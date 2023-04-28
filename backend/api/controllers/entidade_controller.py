class EntidadeController:
    def __init__(self, entidade_repository):
        self.entidade_repository = entidade_repository

    def cria_entidade(self, entidade):
        return self.entidade_repository.cria(entidade)

    def obtem_entidade(self, id):
        return self.entidade_repository.obtem(id)

    def lista_entidade(self):
        return self.entidade_repository.lista()

    def atualiza_entidade(self, entidade, id):
        return self.entidade_repository.atualiza(entidade, id)

    def deleta_entidade(self, id):
        return self.entidade_repository.deleta(id)
