from json import dumps

from repositories.base_repository import BaseRepository
from exceptions.registro_nao_encontrado import RegistroNaoEncontradoException


class ArtefatoRepository(BaseRepository):
    def __init__(self, pool):
        super().__init__(pool)

    def cria(self, artefato):
        if artefato.comportamentos:
            artefato.comportamentos = dumps(artefato.comportamentos)

        query = '''
            WITH artefatos AS (
                INSERT INTO artefatos
                    (tipo, entidade, descricao, ativo, comportamentos)
                VALUES
                    (%s, %s, %s, %s, %s)
                RETURNING
                    *
            ),
            entidades AS (
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
            )
            SELECT
                a.id,
                ROW_TO_JSON(tda.*) AS tipo,
                ROW_TO_JSON(e.*) AS entidade,
                a.descricao,
                a.comportamentos,
                a.ativo,
                a.criado_em,
                a.atualizado_em
            FROM
                artefatos a
            INNER JOIN tipos_de_artefato tda ON
                tda.id = a.tipo
            INNER JOIN entidades e ON
                e.id = a.entidade
        '''
        resultado = self.executa(query, argumentos=[artefato.tipo,
                                                    artefato.entidade,
                                                    artefato.descricao,
                                                    artefato.ativo,
                                                    artefato.comportamentos],
                                 retorna_resultados=True)
        return dict(resultado[0])

    def obtem(self, id):
        query = '''
            WITH entidades AS (
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
            )
            SELECT
                a.id,
                ROW_TO_JSON(tda.*) AS tipo,
                ROW_TO_JSON(e.*) AS entidade,
                a.descricao,
                a.comportamentos,
                a.ativo,
                a.criado_em,
                a.atualizado_em
            FROM
                artefatos a
            INNER JOIN tipos_de_artefato tda ON
                tda.id = a.tipo
            INNER JOIN entidades e ON
                e.id = a.entidade
            WHERE
                a.id = %s
        '''
        resultado = self.executa(query, argumentos=[id],
                                 retorna_resultados=True)
        if not resultado:
            raise RegistroNaoEncontradoException(id)

        return dict(resultado[0])

    def lista(self):
        query = '''
            WITH entidades AS (
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
            )
            SELECT
                a.id,
                ROW_TO_JSON(tda.*) AS tipo,
                ROW_TO_JSON(e.*) AS entidade,
                a.descricao,
                a.comportamentos,
                a.ativo,
                a.criado_em,
                a.atualizado_em
            FROM
                artefatos a
            INNER JOIN tipos_de_artefato tda ON
                tda.id = a.tipo
            INNER JOIN entidades e ON
                e.id = a.entidade
            ORDER BY a.criado_em DESC
        '''
        resultado = self.executa(query, argumentos=[id],
                                 retorna_resultados=True)
        return resultado

    def atualiza(self, artefato, id):
        if artefato.comportamentos:
            artefato.comportamentos = dumps(artefato.comportamentos)

        query = '''
            WITH artefatos AS (
                UPDATE artefatos
                SET tipo = %s,
                    entidade = %s,
                    descricao = %s,
                    ativo = %s,
                    comportamentos = %s
                WHERE
                    id = %s
                RETURNING
                    *
            ),
            entidades AS (
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
            )
            SELECT
                a.id,
                ROW_TO_JSON(tda.*) AS tipo,
                ROW_TO_JSON(e.*) AS entidade,
                a.descricao,
                a.comportamentos,
                a.ativo,
                a.criado_em,
                a.atualizado_em
            FROM
                artefatos a
            INNER JOIN tipos_de_artefato tda ON
                tda.id = a.tipo
            INNER JOIN entidades e ON
                e.id = a.entidade
        '''
        resultado = self.executa(query, argumentos=[artefato.tipo,
                                                    artefato.entidade,
                                                    artefato.descricao,
                                                    artefato.ativo,
                                                    artefato.comportamentos,
                                                    id],
                                 retorna_resultados=True)
        return dict(resultado[0])

    def deleta(self, id):
        query = '''
            DELETE FROM
                artefatos
            WHERE
                id = %s
        '''
        self.executa(query, argumentos=[id])
