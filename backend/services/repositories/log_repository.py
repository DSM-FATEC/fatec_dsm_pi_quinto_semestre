from models.log_model import LogModel
from repositories.base_repository import BaseRepository


class LogRepository(BaseRepository):
    def __init__(self, pool):
        super().__init__(pool)

    def cria(self, log: LogModel) -> None:
        query = '''
            INSERT INTO logs
                (nivel, mensagem)
            VALUES
                (%s, %s)
        '''

        try:
            self.executa(query, argumentos=[log.nivel, log.mensagem])
        except:
            pass