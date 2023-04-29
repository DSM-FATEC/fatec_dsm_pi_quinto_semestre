from repositories.base_repository import BaseRepository
from exceptions.registro_nao_encontrado import RegistroNaoEncontradoException


class TipoEntidadeRepository(BaseRepository):
    def __init__(self, pool):
        super().__init__(pool)

    def cria(self, tipo_entidade):
        query = '''
            INSERT INTO tipos_de_entidade
                (descricao)
            VALUES
                (%s)
            RETURNING
                *
        '''
        resultado = self.executa(query, argumentos=[tipo_entidade.descricao],
                                 retorna_resultados=True)

        return resultado

    def obtem(self, id):
        query = '''
            SELECT
                *
            FROM
                tipos_de_entidade
            WHERE
                id = %s
        '''
        resultado = self.executa(query, argumentos=[id],
                                 retorna_resultados=True)
        if not resultado:
            raise RegistroNaoEncontradoException(id)

        return resultado[0]

    def lista(self):
        query = '''
            SELECT
                *
            FROM
                tipos_de_entidade
            ORDER BY criado_em DESC
        '''
        resultado = self.executa(query, retorna_resultados=True)

        return resultado

    def atualiza(self, tipo_entidade, id):
        query = '''
            UPDATE
                tipos_de_entidade
            SET
                descricao = %s
            WHERE
                id = %s
            RETURNING
                *
        '''
        resultado = self.executa(query, argumentos=[tipo_entidade.descricao, id],
                                 retorna_resultados=True)

        return resultado

    def deleta(self, id):
        query = 'DELETE FROM tipos_de_entidade WHERE id = %s'

        self.executa(query, argumentos=[id])
