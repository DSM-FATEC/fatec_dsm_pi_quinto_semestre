from abc import ABC

from psycopg2.extras import RealDictCursor


# Classe que servirá de base para todos os repositórios, para evitar ter
# quer repetir sempre as mesmas estruturas
class BaseRepository(ABC):
    def __init__(self, pool):
        self.pool = pool

    # Método que executa uma query no banco dos dados, opcionalmente retornando
    # os resultados da query
    def executa(self, query, argumentos=[], retorna_resultados=False):
        # <pool>.getcoon() -> Obtém uma conexão da pool de conexões
        with self.pool.getconn() as conn:
            # <conexão>.cursor() -> Abre um novo um cursor, que é a classe que
            # realmente vai executar as queries no banco de dados
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                try:
                    # <cursor>.execute() -> Prepara um query no banco de dados
                    cursor.execute(query, argumentos)

                    # <conexão>.commit() -> Executa a query preparada no banco de dados
                    conn.commit()

                    if retorna_resultados:
                        # <cursor>.fetchall() -> Retorna os resultados da query
                        # executada pelo cursor
                        return cursor.fetchall()

                    return None
                except Exception as e:
                    # <conexão>.rollback() -> Desfaz todas as alterações realizadas
                    # no banco de dados
                    conn.rollback()
                    raise e
                finally:
                    self.pool.putconn(conn)
