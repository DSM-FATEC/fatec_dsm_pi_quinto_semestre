import logging
from asyncio import run
from json import loads

from models.evento_model import EventoModel


class EventosConsumer:
    def __init__(self, canal, fila, evento_repository, websocket_conector = None):
        self.canal = canal
        self.fila = fila
        self.evento_repository = evento_repository
        self.websocket_conector = websocket_conector

    def consome_eventos(self):
        def processa_evento(canal, metodo, propriedades, corpo):
            try:
                # Converte a mensagem de string para dict
                mensagem = loads(corpo)

                # Cria um novo model com base na mensagem convertida em dict
                evento = EventoModel(artefato=mensagem['artefato'],
                                     corpo=mensagem['corpo'])

                # Salva o evento no banco de dados
                novo_evento = self.evento_repository.cria(evento)
                if not novo_evento['artefato']['ativo']:
                    # Ignora artefatos que não estão ativos
                    return

                if self.websocket_conector:
                    if self.websocket_conector.conexoes_ativas:
                        self.websocket_conector.envia_mensagem_para_todos(novo_evento)

                # Verifica se o canal ainda está aberto
                if canal.is_open:
                    # Marca a mensagem como lida
                    canal.basic_ack(metodo.delivery_tag)
            except IndexError:
                logging.error(e)
                pass
            except Exception as e:
                logging.error(e)
                # Ignora mensagens que tiveram erro de parseamento
                pass

            # TODO

        self.canal.basic_consume(queue=self.fila,
                                 auto_ack=False,
                                 on_message_callback=processa_evento,
                                 exclusive=True)

        try:
            self.canal.start_consuming()
        except KeyboardInterrupt:
            self.canal.stop_consuming()
