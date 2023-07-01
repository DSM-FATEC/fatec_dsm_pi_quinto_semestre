class TipoArtefatoController:
    def __init__(self, tipo_artefato_repository):
        self.tipo_artefato_repository = tipo_artefato_repository

    def cria_tipo_artefato(self, tipo_artefato):
        return self.tipo_artefato_repository.cria(tipo_artefato)

    def obtem_tipo_artefato(self, id):
        return self.tipo_artefato_repository.obtem(id)

    def lista_tipo_artefato(self):
        return self.tipo_artefato_repository.lista()

    def atualiza_tipo_artefato(self, tipo_artefato, id):
        return self.tipo_artefato_repository.atualiza(tipo_artefato, id)

    def deleta_tipo_artefato(self, id):
        return self.tipo_artefato_repository.deleta(id)
