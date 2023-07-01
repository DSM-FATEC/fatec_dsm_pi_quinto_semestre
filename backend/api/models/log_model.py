from datetime import datetime

from pydantic import BaseModel, validator

from validacoes.validador import Validador


class LogModel(BaseModel):
    id: int | None = None
    nivel: str
    mensagem: str
    criado_em: datetime | None = None
    atualizado_em: datetime | None = None

    @validator('nivel')
    def valida_nivel(cls, valor):
        Validador.existe_em(valor, 'nivel', [
            'info',
            'erro',
            'debug',
            'aviso',
        ])

        return valor
