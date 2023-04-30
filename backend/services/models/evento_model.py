from datetime import datetime

from pydantic import BaseModel

from models.artefato_model import ArtefatoSchema


class EventoModel(BaseModel):
    id: int | None = None
    artefato: int
    corpo: dict | None = None
    criado_em: datetime | None = None
    atualizado_em: datetime | None = None


class EventoSchema(EventoModel):
    artefato: ArtefatoSchema
