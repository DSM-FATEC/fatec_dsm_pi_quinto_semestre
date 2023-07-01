from datetime import datetime

from pydantic import BaseModel, validator

from validacoes.validador import Validador


class TipoArtefatoModel(BaseModel):
    id: int | None = None
    descricao: str
    produtor: bool
    criado_em: datetime | None = None
    atualizado_em: datetime | None = None

    @validator('descricao')
    def valida_descricao(cls, valor):
        Validador.max(valor, 'descricao', 100)

        return valor

    @validator('produtor')
    def valida_produtor(cls, valor):
        Validador.not_null(valor, 'produtor')

        return valor
