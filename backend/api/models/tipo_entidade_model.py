from datetime import datetime

from pydantic import BaseModel, validator

from validacoes.validador import Validador


# Declara um modelo que será usado para pegar os dados da requisição
class TipoEntidadeModel(BaseModel):
    id: int | None = None
    descricao: str
    criado_em: datetime | None = None
    atualizado_em: datetime | None = None

    @validator('descricao')
    def valida_descricao(cls, valor):
        Validador.max(valor, 'descricao', 255)

        return valor
