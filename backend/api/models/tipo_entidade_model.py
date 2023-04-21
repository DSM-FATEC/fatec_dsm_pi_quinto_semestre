from datetime import datetime

from pydantic import BaseModel


# Declara um modelo que será usado para pegar os dados da requisição
class TipoEntidadeModel(BaseModel):
    id: int | None = None
    descricao: str
    criado_em: datetime | None = None
    atualizado_em: datetime | None = None
