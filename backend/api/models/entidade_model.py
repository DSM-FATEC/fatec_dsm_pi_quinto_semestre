from datetime import datetime

from pydantic import BaseModel, validator

from validacoes.validador import Validador
from models.tipo_entidade_model import TipoEntidadeModel


class EntidadeModel(BaseModel):
    id: int | None = None
    tipo: int
    descricao: str
    cep: str
    complemento: str | None = None
    bairro: str
    endereco: str
    cidade: str
    estado: str
    criado_em: datetime | None = None
    atualizado_em: datetime | None = None

    @validator('descricao')
    def valida_descricao(cls, valor):
        Validador.filled(valor, 'descricao')
        Validador.max(valor, 'descricao', 255)

        return valor

    @validator('cep')
    def valida_cep(cls, valor):
        Validador.filled(valor, 'cep')
        Validador.max(valor, 'cep', 9)
        Validador.regex(valor, 'cep', r'[0-9]{5}-[0-9]{3}')

        return valor

    @validator('complemento')
    def valida_complemento(cls, valor):
        if valor:  # Só valida caso esteja preenchido
            Validador.max(valor, 'complemento', 255)

        return valor

    @validator('endereco')
    def valida_endereco(cls, valor):
        Validador.filled(valor, 'endereco')
        Validador.max(valor, 'endereco', 255)

        return valor

    @validator('bairro')
    def valida_bairro(cls, valor):
        Validador.filled(valor, 'bairro')
        Validador.max(valor, 'bairro', 255)

        return valor

    @validator('cidade')
    def valida_cidade(cls, valor):
        Validador.filled(valor, 'cidade')
        Validador.max(valor, 'cidade', 255)

        return valor

    @validator('estado')
    def valida_estado(cls, valor):
        Validador.filled(valor, 'estado')
        Validador.max(valor, 'estado', 255)

        return valor


class EntidadeSchema(EntidadeModel):
    tipo: TipoEntidadeModel
