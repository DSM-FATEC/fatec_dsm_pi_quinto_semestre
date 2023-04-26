from models.tipo_entidade_model import TipoEntidadeModel


class TipoEntidadeController:
    def __init__(self, tipo_entidade_repository):
        self.tipo_entidade_repository = tipo_entidade_repository

    def cria_tipo_entidade(self, dados: TipoEntidadeModel):
        return self.tipo_entidade_repository.cria(dados)

    def obtem_tipo_entidade(self, id):
        return self.tipo_entidade_repository.obtem(id)

    def lista_tipo_entidade(self):
        return self.tipo_entidade_repository.lista()

    def atualiza_tipo_entidade(self):
        ...

    def deleta_tipo_entidade(self):
        ...
