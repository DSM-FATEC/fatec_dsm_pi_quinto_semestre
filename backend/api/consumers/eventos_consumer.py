from json import loads
from time import sleep

from models.evento_model import EventoModel
from pika.channel import Channel
from logger.db_logger import DbLogger


class EventosConsumer:
    def __init__(self, canal: Channel, fila, evento_repository,
                 websocket_conector = None, logger: DbLogger = None):
        self.canal = canal
        self.fila = fila
        self.evento_repository = evento_repository
        self.websocket_conector = websocket_conector
        self.logger = logger

    def consome_eventos(self):
        def processa_evento(canal: Channel, metodo, propriedades, corpo: bytes):
            try:
                # Cria um novo model com base na mensagem convertida em dict
                evento = EventoModel.cria_por_evento(corpo)

                # Salva o evento no banco de dados
                novo_evento = self.evento_repository.cria(evento)

                # Ignora mensagem caso o artefato não esteja ativo
                if not novo_evento['artefato']['ativo']:
                    return

                if self.websocket_conector:
                    self.websocket_conector.envia_mensagem_para_todos(novo_evento)
            except Exception as e:
                self.logger.erro(e)

        try:
            # Consome a fila de eventos, removendo (ack) automaticamente
            # as mensagens dela
            self.canal.basic_consume(queue='eventos',
                                     on_message_callback=processa_evento,
                                     auto_ack=True)
            self.canal.start_consuming()
        except Exception as e:
            self.logger.erro(e)
            # Dispara novamente o erro
            raise e
        finally:
            self.canal.stop_consuming()
