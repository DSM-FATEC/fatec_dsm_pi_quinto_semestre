from os import getenv

from psycopg2.pool import ThreadedConnectionPool


class ConectorBancoDeDados:
    def __init__(self):
        # Inicializa as variáveis de configuração do banco sempre que a
        # classe conectora for instanciada
        self.user = getenv('POSTGRES_USER')
        self.password = getenv('POSTGRES_PASSWORD')
        self.host = getenv('POSTGRES_HOST')
        self.port = getenv('POSTGRES_PORT')
        self.db = getenv('POSTGRES_DB')

    # Função que abre uma pool de conexões com o banco
    def abre_pool(self):
        return ThreadedConnectionPool(1, 2, user=self.user,
                                      password=self.password,
                                      host=self.host,
                                      port=self.port,
                                      database=self.db)