from os import getenv

from psycopg2.pool import ThreadedConnectionPool


class BancoDeDadosConector:
    def __init__(self):
        # Inicializa as variáveis de configuração do banco sempre que a
        # classe conectora for instanciada
        self.usuario = getenv('POSTGRES_USER')
        self.senha = getenv('POSTGRES_PASSWORD')
        self.host = getenv('POSTGRES_HOST')
        self.porta = getenv('POSTGRES_PORT')
        self.banco = getenv('POSTGRES_DB')

    # Função que abre uma pool de conexões com o banco
    def abre_pool(self):
        return ThreadedConnectionPool(1, 1000, user=self.usuario,
                                      password=self.senha,
                                      host=self.host,
                                      port=self.porta,
                                      database=self.banco)