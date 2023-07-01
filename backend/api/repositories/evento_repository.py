from json import dumps

from repositories.base_repository import BaseRepository
from exceptions.registro_nao_encontrado import RegistroNaoEncontradoException


class EventoRepository(BaseRepository):
    def __init__(self, pool):
        super().__init__(pool)

    def cria(self, evento):
        if isinstance(evento.corpo, dict):
            evento.corpo = dumps(evento.corpo)

        query = '''
            WITH eventos AS (
                INSERT INTO eventos
                    (artefato, corpo)
                VALUES
                    (%s, %s)
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
            ),
            artefatos AS (
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
            )
            SELECT
                ev.id,
                ROW_TO_JSON(a.*) AS artefato,
                ev.corpo,
                ev.criado_em,
                ev.atualizado_em
            FROM
                eventos ev
            INNER JOIN artefatos a ON
                a.id = ev.artefato
        '''
        resultado = self.executa(query, argumentos=[evento.artefato,
                                                    evento.corpo],
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
            ),
            artefatos AS (
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
            )
            SELECT
                ev.id,
                ROW_TO_JSON(a.*) AS artefato,
                ev.corpo,
                ev.criado_em,
                ev.atualizado_em
            FROM
                eventos ev
            INNER JOIN artefatos a ON
                a.id = ev.artefato
            WHERE
                ev.id = %s
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
            ),
            artefatos AS (
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
            )
            SELECT
                ev.id,
                ROW_TO_JSON(a.*) AS artefato,
                ev.corpo,
                ev.criado_em,
                ev.atualizado_em
            FROM
                eventos ev
            INNER JOIN artefatos a ON
                a.id = ev.artefato
        '''
        resultado = self.executa(query, argumentos=[id],
                                 retorna_resultados=True)

        return resultado


    def atualiza(self, evento, id):
        if isinstance(evento.corpo, dict):
            evento.corpo = dumps(evento.corpo)

        query = '''
            WITH eventos AS (
                UPDATE eventos
                SET artefato = %s,
                    corpo = %s
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
            ),
            artefatos AS (
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
            )
            SELECT
                ev.id,
                ROW_TO_JSON(a.*) AS artefato,
                ev.corpo,
                ev.criado_em,
                ev.atualizado_em
            FROM
                eventos ev
            INNER JOIN artefatos a ON
                a.id = ev.artefato
        '''
        resultado = self.executa(query, argumentos=[evento.artefato,
                                                    evento.corpo,
                                                    id],
                                 retorna_resultados=True)

        return dict(resultado[0])

    def deleta(self, id):
        query = '''
            DELETE FROM
                eventos
            WHERE
                id = %s
        '''
        self.executa(query, argumentos=[id])
