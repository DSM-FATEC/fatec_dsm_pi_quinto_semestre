from json import loads

from repositories.base_repository import BaseRepository
from exceptions.registro_nao_encontrado import RegistroNaoEncontradoException


class EntidadeRepository(BaseRepository):
    def __init__(self, pool):
        super().__init__(pool)

    def cria(self, entidade):
        query = '''
            WITH entidades AS (
                INSERT INTO entidades
                    (tipo, descricao, cep, complemento, bairro, endereco, cidade, estado)
                VALUES
                    (%s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING
                    *
            )
            SELECT
                e.id,
                ROW_TO_JSON(tde.*) AS tipo,
                e.descricao,
                e.cep,
                e.complemento,
                e.endereco,
                e.bairro,
                e.cidade,
                e.estado,
                e.criado_em,
                e.atualizado_em
            FROM
                entidades e
            INNER JOIN tipos_de_entidade tde ON
                tde.id = e.tipo
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

        return dict(resultado[0])

    def obtem(self, id):
        query = '''
            SELECT
                e.id,
                ROW_TO_JSON(tde.*) AS tipo,
                e.descricao,
                e.cep,
                e.complemento,
                e.endereco,
                e.bairro,
                e.cidade,
                e.estado,
                e.criado_em,
                e.atualizado_em
            FROM
                entidades e
            INNER JOIN tipos_de_entidade tde ON
                tde.id = e.tipo
            WHERE
                e.id = %s
        '''
        resultado = self.executa(query, argumentos=[id],
                                 retorna_resultados=True)
        if not resultado:
            raise RegistroNaoEncontradoException(id)

        return dict(resultado[0])

    def lista(self):
        query = '''
            SELECT
                e.id,
                ROW_TO_JSON(tde.*) AS tipo,
                e.descricao,
                e.cep,
                e.complemento,
                e.endereco,
                e.bairro,
                e.cidade,
                e.estado,
                e.criado_em,
                e.atualizado_em
            FROM
                entidades e
            INNER JOIN tipos_de_entidade tde ON
                tde.id = e.tipo
            ORDER BY e.criado_em DESC
        '''
        resultado = self.executa(query, argumentos=[id],
                                 retorna_resultados=True)
        return resultado

    def atualiza(self, entidade, id):
        query = '''
            WITH entidades AS (
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
            )
            SELECT
                e.id,
                ROW_TO_JSON(tde.*) AS tipo,
                e.descricao,
                e.cep,
                e.complemento,
                e.endereco,
                e.bairro,
                e.cidade,
                e.estado,
                e.criado_em,
                e.atualizado_em
            FROM
                entidades e
            INNER JOIN tipos_de_entidade tde ON
                tde.id = e.tipo
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
