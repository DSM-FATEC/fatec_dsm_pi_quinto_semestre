from datetime import datetime

from pydantic import BaseModel, validator
from validacoes.validador import Validador


class UsuarioModel(BaseModel):
    id: int | None
    id_google: str | None
    nome: str
    email: str
    senha: str
    foto: str | None = None
    criado_em: datetime | None = None
    atualizado_em: datetime | None = None

    @validator('id_google')
    def valida_id_google(cls, valor):
        if valor:
            Validador.filled(valor, 'id_google')
            Validador.max(valor, 'id_google', 100)

        return valor

    @validator('nome')
    def valida_nome(cls, valor):
        Validador.filled(valor, 'nome')
        Validador.max(valor, 'nome', 255)

        return valor

    @validator('email')
    def valida_email(cls, valor):
        Validador.filled(valor, 'email')
        Validador.max(valor, 'email', 255)

        return valor

    @validator('senha')
    def valida_senha(cls, valor):
        Validador.filled(valor, 'email')
        Validador.max(valor, 'email', 255)

        return valor


class UsuarioSchema(BaseModel):
    id: int | None
    id_google: str | None
    nome: str
    email: str
    foto: str | None
    criado_em: datetime | None
    atualizado_em: datetime | None
