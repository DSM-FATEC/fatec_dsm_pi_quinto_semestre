from models.evento_model import EventoModel, EventoSchema


class EventoController:
    def __init__(self, evento_repository):
        self.evento_repository = evento_repository

    def cria_evento(self, evento):
        return self.evento_repository.cria(evento)

    def obtem_evento(self, id):
        return self.evento_repository.obtem(id)

    def lista_evento(self):
        return self.evento_repository.lista()

    def atualiza_evento(self, evento, id):
        return self.evento_repository.atualiza(evento, id)

    def deleta_evento(self, id):
        return self.evento_repository.deleta(id)