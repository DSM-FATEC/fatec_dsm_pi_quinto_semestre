from datetime import datetime

from pydantic import BaseModel, validator

from validacoes.validador import Validador
from models.tipo_artefato_model import TipoArtefatoModel
from models.entidade_model import EntidadeModel


class ArtefatoModel(BaseModel):
    id: int | None
    tipo: int
    entidade: int
    ativo: bool | None = False
    descricao: str | None = None
    comportamentos: dict | None = None
    criado_em: datetime | None = None
    atualizado_em: datetime | None = None

    @validator('tipo')
    def valida_tipo(cls, valor):
        Validador.filled(valor, 'tipo')

        return valor

    @validator('entidade')
    def valida_entidade(cls, valor):
        Validador.filled(valor, 'entidade')

        return valor

    @validator('descricao')
    def valida_descricao(cls, valor):
        if valor:  # Só valida caso esteja preenchido
            Validador.max(valor, 'descricao', 255)

        return valor


class ArtefatoSchema(ArtefatoModel):
    tipo: TipoArtefatoModel
    entidade: EntidadeModel
