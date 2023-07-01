class AuthController:
    def __init__(self, usuario_repository) -> None:
        self.usuario_repository = usuario_repository

    def autoriza(self, email: str, senha: str) -> bool:
        return self.usuario_repository.autoriza(email, senha)
