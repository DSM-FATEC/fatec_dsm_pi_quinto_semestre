from models.evento_model import EventoModel, EventoSchema


class EventoController:
    def __init__(self, evento_repository, websocket_conector = None):
        self.evento_repository = evento_repository
        self.websocket_conector = websocket_conector

    def cria_evento(self, evento):
        novo_evento = self.evento_repository.cria(evento)

        try:
            if not novo_evento['artefato']['ativo']:
                return novo_evento

            if self.websocket_conector:
                if self.websocket_conector.conexoes_ativas:
                    self.websocket_conector.envia_mensagem_para_todos(novo_evento)
        except IndexError:
            pass

        return novo_evento

    def obtem_evento(self, id):
        return self.evento_repository.obtem(id)

    def lista_evento(self):
        return self.evento_repository.lista()

    def atualiza_evento(self, evento, id):
        return self.evento_repository.atualiza(evento, id)

    def deleta_evento(self, id):
        return self.evento_repository.deleta(id)