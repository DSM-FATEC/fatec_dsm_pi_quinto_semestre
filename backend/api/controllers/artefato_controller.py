class ArtefatoController:
    def __init__(self, artefato_repository):
        self.artefato_repository = artefato_repository

    def cria_artefato(self, entidade):
        return self.artefato_repository.cria(entidade)

    def obtem_artefato(self, id):
        return self.artefato_repository.obtem(id)

    def lista_artefato(self):
        return self.artefato_repository.lista()

    def atualiza_artefato(self, entidade, id):
        return self.artefato_repository.atualiza(entidade, id)

    def deleta_artefato(self, id):
        return self.artefato_repository.deleta(id)
