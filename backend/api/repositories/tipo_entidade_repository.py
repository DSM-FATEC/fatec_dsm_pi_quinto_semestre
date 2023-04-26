from repositories.base_repository import BaseRepository


class TipoEntidadeRepository(BaseRepository):
    def __init__(self, pool):
        super().__init__(pool)

    def cria(self, entidade):
        query = '''
            INSERT INTO tipos_de_entidade (descricao)
            VALUES (%s)
            RETURNING *
        '''
        resultado = self.executa(query, argumentos=[entidade.descricao],
                                 retorna_resultados=True)

        return resultado

    def obtem(self, id):
        query = '''
            SELECT *
            FROM tipos_de_entidade
            WHERE id = %s
        '''
        resultado = self.executa(query, argumentos=[id],
                                 retorna_resultados=True)

        return resultado

    def lista(self):
        query = 'SELECT * FROM tipos_de_entidade'
        resultado = self.executa(query, retorna_resultados=True)

        return resultado

    def atualiza(self, entidade):
        ...

    def deleta(self, id):
        ...
