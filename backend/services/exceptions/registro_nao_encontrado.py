class RegistroNaoEncontradoException(Exception):
    def __init__(self, id, *args):
        super().__init__(*args)

        self.id = id

    def __str__(self) :
        return f'Não foram encontrados registros para o id {self.id}'