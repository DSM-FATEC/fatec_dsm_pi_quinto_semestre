from repositories.base_repository import BaseRepository


class TipoArtefatoRepository(BaseRepository):
    def __init__(self, pool):
        super().__init__(pool)

    def cria(self, tipo_artefato):
        query = '''
            INSERT INTO tipos_de_artefato
                (descricao, produtor)
            VALUES
                (%s, %s)
            RETURNING
                *
        '''
        resultado = self.executa(query, argumentos=[tipo_artefato.descricao,
                                                    tipo_artefato.produtor],
                                 retorna_resultados=True)

        return resultado

    def obtem(self, id):
        query = '''
            SELECT
                *
            FROM
                tipos_de_artefato
            WHERE
                id = %s
        '''
        resultado = self.executa(query, argumentos=[id],
                                 retorna_resultados=True)

        return resultado

    def lista(self):
        query = 'SELECT * FROM tipos_de_artefato'
        resultado = self.executa(query, retorna_resultados=True)

        return resultado

    def atualiza(self, tipo_artefato, id):
        query = '''
            UPDATE
                tipos_de_artefato
            SET
                descricao = %s,
                produtor = %s
            WHERE
                id = %s
            RETURNING
                *
        '''
        resultado = self.executa(query, argumentos=[tipo_artefato.descricao,
                                                    tipo_artefato.produtor,
                                                    id],
                                 retorna_resultados=True)

        return resultado

    def deleta(self, id):
        query = 'DELETE FROM tipos_de_artefato WHERE id = %s'

        self.executa(query, argumentos=[id])
