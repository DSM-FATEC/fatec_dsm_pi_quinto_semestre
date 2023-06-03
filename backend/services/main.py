from os import getenv
from secrets import compare_digest
from datetime import datetime
from threading import Thread

# Importando bibliotecas externas
from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.websockets import WebSocket, WebSocketDisconnect
from dotenv import load_dotenv
from pydantic import ValidationError

# Importando classes internas
from consumers.eventos_consumer import EventosConsumer
from controllers.tipo_entidade_controller import TipoEntidadeController
from controllers.entidade_controller import EntidadeController
from controllers.tipo_artefato_controller import TipoArtefatoController
from controllers.artefato_controller import ArtefatoController
from controllers.evento_controller import EventoController
from controllers.usuario_controller import UsuarioController
from controllers.auth_controller import AuthController
from conectors.banco_de_dados_conector import BancoDeDadosConector
from conectors.websocket_connector import WebsocketConnector
from conectors.rabbitmq_conector import RabbitMqConector
from exceptions.registro_nao_encontrado import RegistroNaoEncontradoException
from exceptions.usuario_invalido import UsuarioInvalidoException
from models.tipo_entidade_model import TipoEntidadeModel
from models.entidade_model import EntidadeModel, EntidadeSchema
from models.tipo_artefato_model import TipoArtefatoModel
from models.artefato_model import ArtefatoModel, ArtefatoSchema
from models.evento_model import EventoModel, EventoSchema
from models.usuario_model import UsuarioModel, UsuarioSchema
from repositories.tipo_entidade_repository import TipoEntidadeRepository
from repositories.entidade_repository import EntidadeRepository
from repositories.tipo_artefato_repository import TipoArtefatoRepository
from repositories.artefato_repository import ArtefatoRepository
from repositories.evento_repository import EventoRepository
from repositories.usuario_repository import UsuarioRepository


# Carrega o arquivo de configurações, tornando as variáveis presentes
# nele acessíveis usando os.environ ou os.getenv()
load_dotenv()

# Criando a variável global que o FastAPI vai usar como ponto de entrada
app = FastAPI()

# Criando a variável global de segurancao do FastaPI
security = HTTPBasic()

# Instancia conectores
websockets_conector = WebsocketConnector()
banco_de_dados_conector = BancoDeDadosConector()
rabbit_mq_conector = RabbitMqConector()

# Conectando ao banco de dados e abrindo uma pool de conexões
pool = banco_de_dados_conector.abre_pool()

# # Conecta no rabbit mq
# eventos_canal, eventos_fila = rabbit_mq_conector.abre_canal('eventos_exchange',
#                                                             nome_fila='eventos',
#                                                             conecta_amq_topic=True)

# Instanciando os repositórios
tipo_entidade_repository = TipoEntidadeRepository(pool)
entidade_repository = EntidadeRepository(pool)
tipo_artefato_repository = TipoArtefatoRepository(pool)
artefato_repository = ArtefatoRepository(pool)
evento_repository = EventoRepository(pool)
usuario_repository = UsuarioRepository(pool)

# Instanciando os controllers
tipo_entidade_controller = TipoEntidadeController(tipo_entidade_repository)
entidade_controller = EntidadeController(entidade_repository)
tipo_artefato_controller = TipoArtefatoController(tipo_artefato_repository)
artefato_controller = ArtefatoController(artefato_repository)
evento_controller = EventoController(evento_repository, websockets_conector)
usuario_controller = UsuarioController(usuario_repository)
auth_controller = AuthController(usuario_repository)


# Registrando os middlewares
@app.middleware('http')
async def lida_com_erros_middleware(requisicao: Request, proximo):
    try:
        return await proximo(requisicao)
    except ValidationError as e:
        return JSONResponse(status_code=422, content={'erro': str(e)})
    except RegistroNaoEncontradoException as e:
        return JSONResponse(status_code=404, content={'erro': str(e)})
    except UsuarioInvalidoException as e:
        return JSONResponse(status_code=401, content={'erro': str(e)})
    except Exception as e:
        return JSONResponse(status_code=500, content={'erro': str(e)})


# Cria funcao que vai validar as credenciais do usuário
def valida_credenciais(credenciais: HTTPBasicCredentials = Depends(security)):
    autorizado = auth_controller.autoriza(credenciais.username, credenciais.password)

    if not autorizado:
        raise UsuarioInvalidoException()

    return credenciais.username



# # Abre consumidor
# eventos_consumer = EventosConsumer(eventos_canal, eventos_fila,
#                                    evento_repository, websockets_conector)

# # Inicia consumidor de eventos
# eventos_consumer_thread = Thread(target=eventos_consumer.consome_eventos,
#                                  name='Consome eventos')
# eventos_consumer_thread.start()


# Endpoints utilitários
@app.get('/ping', tags=['Testes'])
def ping():
    return 'pong'


# Endpoints de tipos de entidade
@app.post('/tipo_entidade', tags=['Tipos de entidade'],
          dependencies=[Depends(valida_credenciais)])
def cria_tipo_entidade(tipo_entidade: TipoEntidadeModel) -> TipoEntidadeModel:
    return tipo_entidade_controller.cria_tipo_entidade(tipo_entidade)


@app.get('/tipo_entidade/{id}', tags=['Tipos de entidade'],
         dependencies=[Depends(valida_credenciais)])
def obtem_tipo_entidade(id) -> TipoEntidadeModel:
    return tipo_entidade_controller.obtem_tipo_entidade(id)


@app.get('/tipo_entidade', tags=['Tipos de entidade'],
         dependencies=[Depends(valida_credenciais)])
def lista_tipo_entidade() -> list[TipoEntidadeModel]:
    return tipo_entidade_controller.lista_tipo_entidade()


@app.put('/tipo_entidade/{id}', tags=['Tipos de entidade'],
         dependencies=[Depends(valida_credenciais)])
def atualiza_tipo_entidade(tipo_entidade: TipoEntidadeModel, id) -> TipoEntidadeModel:
    return tipo_entidade_controller.atualiza_tipo_entidade(tipo_entidade, id)


@app.delete('/tipo_entidade/{id}', tags=['Tipos de entidade'],
            dependencies=[Depends(valida_credenciais)])
def deleta_tipo_entidade(id) -> None:
    return tipo_entidade_controller.deleta_tipo_entidade(id)


# Endpoints de entidade
@app.post('/entidade', tags=['Entidades'],
          dependencies=[Depends(valida_credenciais)])
def cria_entidade(entidade: EntidadeModel) -> EntidadeSchema:
    return entidade_controller.cria_entidade(entidade)


@app.get('/entidade/{id}', tags=['Entidades'],
         dependencies=[Depends(valida_credenciais)])
def obtem_entidade(id) -> EntidadeSchema:
    return entidade_controller.obtem_entidade(id)


@app.get('/entidade', tags=['Entidades'],
         dependencies=[Depends(valida_credenciais)])
def lista_entidade() -> list[EntidadeSchema]:
    return entidade_controller.lista_entidade()


@app.put('/entidade/{id}', tags=['Entidades'],
         dependencies=[Depends(valida_credenciais)])
def atualiza_entidade(entidade: EntidadeModel, id) -> EntidadeSchema:
    return entidade_controller.atualiza_entidade(entidade, id)


@app.delete('/entidade/{id}', tags=['Entidades'],
            dependencies=[Depends(valida_credenciais)])
def deleta_entidade(id) -> None:
    return entidade_controller.deleta_entidade(id)


# Endpoints de tipo de artefatos
@app.post('/tipo_artefato', tags=['Tipos de artefato'],
          dependencies=[Depends(valida_credenciais)])
def cria_tipo_artefato(entidade: TipoArtefatoModel) -> TipoArtefatoModel:
    return tipo_artefato_controller.cria_tipo_artefato(entidade)


@app.get('/tipo_artefato/{id}', tags=['Tipos de artefato'],
         dependencies=[Depends(valida_credenciais)])
def obtem_tipo_artefato(id) -> TipoArtefatoModel:
    return tipo_artefato_controller.obtem_tipo_artefato(id)


@app.get('/tipo_artefato', tags=['Tipos de artefato'],
         dependencies=[Depends(valida_credenciais)])
def lista_tipo_artefato() -> list[TipoArtefatoModel]:
    return tipo_artefato_controller.lista_tipo_artefato()


@app.put('/tipo_artefato/{id}', tags=['Tipos de artefato'],
         dependencies=[Depends(valida_credenciais)])
def atualiza_tipo_artefato(entidade: TipoArtefatoModel, id) -> TipoArtefatoModel:
    return tipo_artefato_controller.atualiza_tipo_artefato(entidade, id)


@app.delete('/tipo_artefato/{id}', tags=['Tipos de artefato'],
            dependencies=[Depends(valida_credenciais)])
def deleta_tipo_artefato(id) -> None:
    return tipo_artefato_controller.deleta_tipo_artefato(id)


# Endpoints de artefato
@app.post('/artefato', tags=['Artefatos'],
          dependencies=[Depends(valida_credenciais)])
def cria_artefato(artefato: ArtefatoModel) -> ArtefatoSchema:
    return artefato_controller.cria_artefato(artefato)


@app.get('/artefato/{id}', tags=['Artefatos'],
         dependencies=[Depends(valida_credenciais)])
def obtem_artefato(id) -> ArtefatoSchema:
    return artefato_controller.obtem_artefato(id)


@app.get('/artefato', tags=['Artefatos'],
         dependencies=[Depends(valida_credenciais)])
def lista_artefato() -> list[ArtefatoSchema]:
    return artefato_controller.lista_artefato()


@app.put('/artefato/{id}', tags=['Artefatos'],
         dependencies=[Depends(valida_credenciais)])
def atualiza_artefato(artefato: ArtefatoModel, id) -> ArtefatoSchema:
    return artefato_controller.atualiza_artefato(artefato, id)


@app.delete('/artefato/{id}', tags=['Artefatos'],
            dependencies=[Depends(valida_credenciais)])
def deleta_artefato(id) -> None:
    return artefato_controller.deleta_artefato(id)


# Endpoints de evento
@app.post('/evento', tags=['Eventos'],
          dependencies=[Depends(valida_credenciais)])
def cria_evento(artefato: EventoModel) -> EventoSchema:
    return evento_controller.cria_evento(artefato)


@app.get('/evento/{id}', tags=['Eventos'],
         dependencies=[Depends(valida_credenciais)])
def obtem_evento(id) -> EventoSchema:
    return evento_controller.obtem_evento(id)


@app.get('/evento', tags=['Eventos'],
         dependencies=[Depends(valida_credenciais)])
def lista_evento() -> list[EventoSchema]:
    return evento_controller.lista_evento()


@app.put('/evento/{id}', tags=['Eventos'],
         dependencies=[Depends(valida_credenciais)])
def atualiza_evento(artefato: EventoModel, id) -> EventoSchema:
    return evento_controller.atualiza_evento(artefato, id)


@app.delete('/evento/{id}', tags=['Eventos'],
            dependencies=[Depends(valida_credenciais)])
def deleta_evento(id) -> None:
    return evento_controller.deleta_evento(id)


# Endpoints de usuarios
@app.post('/usuario', tags=['Usuarios'])
def cria_usuario(usuario: UsuarioModel) -> UsuarioSchema:
    return usuario_controller.cria_usuario(usuario)


@app.get('/usuario/{id}', tags=['Usuarios'],
         dependencies=[Depends(valida_credenciais)])
def obtem_usuario(id) -> UsuarioSchema:
    return usuario_controller.obtem_usuario(id)


@app.get('/usuario', tags=['Usuarios'],
         dependencies=[Depends(valida_credenciais)])
def lista_usuario() -> list[UsuarioSchema]:
    return usuario_controller.lista_usuario()


@app.put('/usuario/{id}', tags=['Usuarios'],
         dependencies=[Depends(valida_credenciais)])
def atualiza_usuario(usuario: UsuarioModel, id) -> UsuarioSchema:
    return usuario_controller.atualiza_usuario(usuario, id)


@app.delete('/usuario/{id}', tags=['Usuarios'],
            dependencies=[Depends(valida_credenciais)])
def deleta_usuario(id) -> None:
    return usuario_controller.deleta_usuario(id)


# Websocket de eventos
@app.websocket('/evento/ws/{id}')
async def eventos(websocket: WebSocket, id):
    await websockets_conector.conecta(websocket)

    try:
        while True:
            evento = await websocket.receive_json()

            if isinstance(evento, dict):
                await websockets_conector.envia_mensagem_para_todos(evento)
    except WebSocketDisconnect:
        websockets_conector.desconecta(websocket)
