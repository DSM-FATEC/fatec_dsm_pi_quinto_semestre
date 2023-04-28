class TipoEntidadeController:
    def __init__(self, tipo_entidade_repository):
        self.tipo_entidade_repository = tipo_entidade_repository

    def cria_tipo_entidade(self, tipo_entidade):
        return self.tipo_entidade_repository.cria(tipo_entidade)

    def obtem_tipo_entidade(self, id):
        return self.tipo_entidade_repository.obtem(id)

    def lista_tipo_entidade(self):
        return self.tipo_entidade_repository.lista()

    def atualiza_tipo_entidade(self, tipo_entidade, id):
        return self.tipo_entidade_repository.atualiza(tipo_entidade, id)

    def deleta_tipo_entidade(self, id):
        return self.tipo_entidade_repository.deleta(id)
