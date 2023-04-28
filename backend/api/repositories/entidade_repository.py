from json import loads

from repositories.base_repository import BaseRepository


class EntidadeRepository(BaseRepository):
    def __init__(self, pool):
        super().__init__(pool)

    def cria(self, entidade):
        query = '''
            INSERT INTO entidades
                (tipo, descricao, cep, complemento, bairro, endereco, cidade, estado)
            VALUES
                (%s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING
                *
        '''
        resultado = self.executa(query, argumentos=[entidade.tipo,
                                                    entidade.descricao,
                                                    entidade.cep,
                                                    entidade.complemento,
                                                    entidade.bairro,
                                                    entidade.endereco,
                                                    entidade.cidade,
                                                    entidade.estado],
                                 retorna_resultados=True)

        return resultado

    def obtem(self, id):
        query = '''
            SELECT
                e.*,
                ROW_TO_JSON(tde.*) AS tipo_json
            FROM
                entidades e
            INNER JOIN tipos_de_entidade tde ON
                tde.id = e.tipo
            WHERE
                e.id = %s
        '''
        resultado = self.executa(query, argumentos=[id],
                                 retorna_resultados=True)
        if resultado:
            for entidade in resultado:
                entidade['tipo'] = entidade['tipo_json']
                del entidade['tipo_json']

        return resultado

    def lista(self):
        query = '''
            SELECT
                e.*,
                ROW_TO_JSON(tde.*) AS tipo_json
            FROM
                entidades e
            INNER JOIN tipos_de_entidade tde ON
                tde.id = e.tipo
        '''
        resultado = self.executa(query, argumentos=[id],
                                 retorna_resultados=True)
        if resultado:
            for entidade in resultado:
                entidade['tipo'] = entidade['tipo_json']
                del entidade['tipo_json']

        return resultado

    def atualiza(self, entidade, id):
        query = '''
            UPDATE
                entidades
            SET
                tipo = %s,
                descricao = %s,
                cep = %s,
                complemento = %s,
                bairro = %s,
                endereco = %s,
                cidade = %s,
                estado = %s
            WHERE
                id = %s
            RETURNING
                *
        '''
        resultado = self.executa(query, argumentos=[entidade.tipo,
                                                    entidade.descricao,
                                                    entidade.cep,
                                                    entidade.complemento,
                                                    entidade.bairro,
                                                    entidade.endereco,
                                                    entidade.cidade,
                                                    entidade.estado,
                                                    id],
                                 retorna_resultados=True)

        return resultado

    def deleta(self, id):
        query = 'DELETE FROM entidades WHERE id = %s'

        self.executa(query, argumentos=[id])
