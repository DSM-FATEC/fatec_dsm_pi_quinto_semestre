# Classes implementadas pelo projeto

```mermaid
classDiagram
    class BancoDeDadosConector {
        <<connectors>>

        +usuario: str
        +senha: str
        +host: str
        +port: int
        +banco: int

        +abre_pool(): ThreadedConnectionPool
    }

    class WebsocketConector {
        <<connectors>>

        +conexoes_ativas: list[Websocket]

        +conecta(websocket: Websocket): void
        +desconecta(websocket: Websocket): void
        +envia_mensagem_para_todos(mensagem: dict): void
    }

    class RabbitMqConector {
        <<connector>>

        +usuario: str
        +senha: str
        +host: str
        +porta: str
        +host_virtual: str

        +abre_canal(nome_exchange: str, nome_fila: str, conecta_amq_topic: bool): tuple[Channel, str]
    }

    class BaseModel {
        <<pydantic>>
    }

    class BaseRepository {
        <<abstract>>
        <<repositories>>

        +pool: ThreadedConnectionPool

        +executa(query: str, retorna_resultados: bool, *args: Any)
    }

    class RegistroNaoEncontradoException {
        <<exceptions>>

        +id: int
    }

    class TipoEntidadeModel {
        <<models>>

        +id: int|None
        +descricao: str
        +criado_em: datetime|None
        +atualizado_em: datetime|None

        valida_descricao(valor: str): str
    }

    class EntidadeModel {
        <<models>>

        +id: int|None
        +descricao: str
        +cep: str
        +complemento: str|None
        +bairro: str
        +endereco: str
        +cidade: str
        +estado: str
        +criado_em: datetime|None
        +atualizado_em: datetime|None

        valida_descricao(valor: str): str
        valida_cep(valor: str): str
        valida_complemento(valor: str|None): str|None
        valida_endereco(valor: str): str
        valida_bairro(valor: str): str
        valida_cidade(valor: str): str
        valida_estado(valor: str): str
    }

    class EntidadeSchema {
        <<models>>

        +tipo: TipoEntidadeModel
    }

    class TipoArtefatoModel {
        <<models>>

        +id: int|None
        +descricao: str
        +produtor: bool
        +criado_em: datetime|None
        +atualizado_em: datetime|None

        +valida_descricao(valor: str): str
        +valida_produtor(valor: bool): bool
    }

    class ArtefatoModel {
        <<models>>

        +id: int|None
        +tipo: int
        +entidade: int
        +ativo: bool|None
        +descricao: str|None
        +comportamentos: dict|None
        +criado_em: datetime|None
        +atualizado_em: datetime|None

        +valida_tipo(valor: int): int
        +valida_entidade(valor: int): int
        +valida_descricao(valor: str|None): str|None
    }

    class ArtefatoSchema {
        <<models>>

        +tipo: TipoArtefatoModel
        +entidade: EntidadeSchema
    }

    class EventoModel {
        <<models>>

        +id: int|None
        +artefato: int
        +corpo: dict|None
        +criado_em: datetime|None
        +atualizado_em: datetime|None
    }

    class EventoSchema {
        <<models>>

        +artefato: ArtefatoSchema
    }

    class TipoEntidadeController {
        <<controllers>>

        +tipo_entidade_repository: TipoEntidadeRepository

        +cria_tipo_entidade(tipo_entidade: TipoEntidadeModel): dict
        +obtem_tipo_entidade(id: int): dict
        +lista_tipo_entidade(): list[dict]
        +atualiza_tipo_entidade(tipo_entidade: TipoEntidadeModel, id: int): dict
        +deleta_tipo_entidade(id: int): void
    }

    class EntidadeController {
        <<controllers>>

        +entidade_repository: EntidadeRepository

        +cria_entidade(entidade: EntidadeModel): dict
        +obtem_entidade(id: int): dict
        +lista_entidade(): list[dict]
        +atualiza_entidade(entidade: EntidadeModel, id: int): dict
        +deleta_entidade(id: int): void
    }

    class TipoArtefatoController {
        <<controllers>>

        +tipo_artefato_controller: TipoArtefatoRepository

        +cria_tipo_artefato(tipo_artefato: TipoArtefatoModel): dict
        +obtem_tipo_artefato(id: int): dict
        +lista_tipo_artefato(): list[dict]
        +atualiza_tipo_artefato(tipo_artefato: TipoArtefatoModel, id: int): dict
        +deleta_tipo_artefato(id: int): void
    }

    class ArtefatoController {
        <<controllers>>

        +artefato_repository: ArtefatoRepository

        +cria_artefato(artefato: ArtefatoModel): ArtefatoSchema
        +obtem_artefato(id: int): ArtefatoSchema
        +lista_artefato(): list[ArtefatoSchema]
        +atualiza_artefato(artefato: ArtefatoModel, id: int): ArtefatoSchema
        +deleta_artefato(id: int): void
    }

    class EventoController {
        <<controllers>>

        +evento_repository: EventoRepository
        +websocket_conector: WebsocketConector

        +cria_evento(evento: EventoModel): EventoSchema
        +obtem_evento(id: int): EventoSchema
        +lista_evento(): list[EventoSchema]
        +atualiza_evento(evento: EventoModel, id: int): list[EventoSchema]
        +deleta_evento(id: int): void
    }

    class TipoEntidadeRepository {
        <<repositories>>

        +pool: ThreadedConnectionPool

        +cria(tipo_entidade: TipoEntidadeModel): dict
        +obtem(id: int): dict
        +lista(): list[dict]
        +atualiza(tipo_entidade: TipoEntidadeModel, id: int): dict
        +deleta(id: int): void
    }

    class EntidadeRepository {
        <<repositories>>

        +pool: ThreadedConnectionPool

        +cria(entidade: TipoEntidadeModel): dict
        +obtem(id: int): dict
        +lista(): list[dict]
        +atualiza(entidade: TipoEntidadeModel): dict
        +deleta(id: int): void
    }

    class TipoArtefatoRepository {
        <<repositories>>

        +pool: ThreadedConnectionPool

        +cria(tipo_artefato: TipoArtefatoModel): dict
        +obtem(id: int): dict
        +lista(): list[dict]
        +atualiza(tipo_artefato: TipoArtefatoModel, id: int): dict
        +deleta(id: int): void
    }

    class ArtefatoRepository {
        <<repositories>>

        +pool: ThreadedConnectionPool

        +cria(artefato: ArtefatoModel): ArtefatoSchema
        +obtem(id: int): ArtefatoSchema
        +lista(): list[ArtefatoSchema]
        +atualiza(artefato: ArtefatoModel, id: int): ArtefatoSchema
        +deleta(id: int): void
    }

    class EventoRepository {
        <<repositories>>

        +pool: ThreadedConnectionPool

        +cria(evento: EventoModel): EventoSchema
        +obtem(id: int): EventoSchema
        +lista(): list[EventoSchema]
        +atualiza(evento: EventoModel, id: int): EventoSchema
        +deleta(id: int): void
    }

    TipoEntidadeModel --|> BaseModel
    TipoEntidadeRepository --|> BaseRepository
    TipoEntidadeRepository ..> TipoEntidadeModel
    TipoEntidadeRepository ..> RegistroNaoEncontradoException
    TipoEntidadeController ..> TipoEntidadeModel
    TipoEntidadeController ..> TipoEntidadeRepository

    EntidadeModel --|> BaseModel
    EntidadeSchema --|> EntidadeModel
    EntidadeRepository --|> BaseRepository
    EntidadeRepository ..> EntidadeModel
    EntidadeRepository ..> RegistroNaoEncontradoException
    EntidadeController ..> EntidadeModel
    EntidadeController ..> EntidadeRepository

    TipoArtefatoModel --|> BaseModel
    TipoArtefatoRepository --|> BaseRepository
    TipoArtefatoRepository ..> TipoArtefatoModel
    TipoArtefatoRepository ..> RegistroNaoEncontradoException
    TipoArtefatoController ..> TipoArtefatoModel
    TipoArtefatoController ..> TipoArtefatoRepository

    ArtefatoModel --|> BaseModel
    ArtefatoSchema --|> ArtefatoModel
    ArtefatoSchema ..> EntidadeSchema
    ArtefatoSchema ..> TipoArtefatoModel
    ArtefatoRepository --|> BaseRepository
    ArtefatoRepository ..> ArtefatoModel
    ArtefatoRepository ..> ArtefatoSchema
    ArtefatoRepository ..> RegistroNaoEncontradoException
    ArtefatoController ..> ArtefatoRepository
    ArtefatoController ..> ArtefatoModel

    EventoModel --|> BaseModel
    EventoSchema --|> EventoModel
    EventoSchema ..> ArtefatoSchema
    EventoRepository --|> BaseRepository
    EventoRepository ..> EventoModel
    EventoRepository ..> EventoSchema
    EventoRepository ..> RegistroNaoEncontradoException
    EventoController ..> EventoRepository
    EventoController ..> WebsocketConector
    EventoController ..> EventoModel
```
