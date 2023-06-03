class UsuarioController:
    def __init__(self, usuario_repository):
        self.usuario_repository = usuario_repository

    def cria_usuario(self, usuario):
        return self.usuario_repository.cria(usuario)

    def obtem_usuario(self, id):
        return self.usuario_repository.obtem(id)

    def lista_usuario(self):
        return self.usuario_repository.lista()

    def atualiza_usuario(self, usuario, id):
        return self.usuario_repository.atualiza(usuario, id)

    def deleta_usuario(self, id):
        return self.usuario_repository.deleta(id)
