from datetime import datetime
from json import loads

from pydantic import BaseModel

from models.artefato_model import ArtefatoSchema


class EventoModel(BaseModel):
    id: int | None = None
    artefato: int
    corpo: dict | None = None
    criado_em: datetime | None = None
    atualizado_em: datetime | None = None

    @staticmethod
    def cria_por_evento(evento: str | bytes):
        if isinstance(evento, bytes):
            evento = evento.decode('utf-8')

        dados = loads(evento)

        return EventoModel(artefato=dados['artefato'],
                           corpo=dados['corpo'])


class EventoSchema(EventoModel):
    artefato: ArtefatoSchema
