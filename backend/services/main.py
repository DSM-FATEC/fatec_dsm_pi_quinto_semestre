# Importando bibliotecas externas
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from pydantic import ValidationError

# Importando classes internas
from controllers.tipo_entidade_controller import TipoEntidadeController
from controllers.entidade_controller import EntidadeController
from controllers.tipo_artefato_controller import TipoArtefatoController
from controllers.artefato_controller import ArtefatoController
from controllers.evento_controller import EventoController
from conectors.banco_de_dados_conector import BancoDeDadosConector
from exceptions.registro_nao_encontrado import RegistroNaoEncontradoException
from models.tipo_entidade_model import TipoEntidadeModel
from models.entidade_model import EntidadeModel, EntidadeSchema
from models.tipo_artefato_model import TipoArtefatoModel
from models.artefato_model import ArtefatoModel, ArtefatoSchema
from models.evento_model import EventoModel, EventoSchema
from repositories.tipo_entidade_repository import TipoEntidadeRepository
from repositories.entidade_repository import EntidadeRepository
from repositories.tipo_artefato_repository import TipoArtefatoRepository
from repositories.artefato_repository import ArtefatoRepository
from repositories.evento_repository import EventoRepository


# Carrega o arquivo de configurações, tornando as variáveis presentes
# nele acessíveis usando os.environ ou os.getenv()
load_dotenv()

# Criando a variável global que o FastAPI vai usar como ponto de entrada
app = FastAPI()

# Conectando ao banco de dados e abrindo uma pool de conexões
conector = BancoDeDadosConector()
pool = conector.abre_pool()

# Instanciando os repositórios
tipo_entidade_repository = TipoEntidadeRepository(pool)
entidade_repository = EntidadeRepository(pool)
tipo_artefato_repository = TipoArtefatoRepository(pool)
artefato_repository = ArtefatoRepository(pool)
evento_repository = EventoRepository(pool)

# Instanciando os controllers
tipo_entidade_controller = TipoEntidadeController(tipo_entidade_repository)
entidade_controller = EntidadeController(entidade_repository)
tipo_artefato_controller = TipoArtefatoController(tipo_artefato_repository)
artefato_controller = ArtefatoController(artefato_repository)
evento_controller = EventoController(evento_repository)


# Registrando os middlewares
@app.middleware('http')
async def lida_com_erros_middleware(requisicao: Request, proximo):
    try:
        return await proximo(requisicao)
    except ValidationError as e:
        return JSONResponse(status_code=422, content={'erro': str(e)})
    except RegistroNaoEncontradoException as e:
        return JSONResponse(status_code=404, content={'erro': str(e)})
    except Exception as e:
        return JSONResponse(status_code=500, content={'erro': str(e)})


# Endpoints utilitários
@app.get('/ping', tags=['Testes'])
def ping():
    return 'pong'


# Endpoints de tipos de entidade
@app.post('/tipo_entidade', tags=['Tipos de entidade'])
def cria_tipo_entidade(tipo_entidade: TipoEntidadeModel) -> TipoEntidadeModel:
    return tipo_entidade_controller.cria_tipo_entidade(tipo_entidade)

@app.get('/tipo_entidade/{id}', tags=['Tipos de entidade'])
def obtem_tipo_entidade(id) -> TipoEntidadeModel:
    return tipo_entidade_controller.obtem_tipo_entidade(id)

@app.get('/tipo_entidade', tags=['Tipos de entidade'])
def lista_tipo_entidade() -> list[TipoEntidadeModel]:
    return tipo_entidade_controller.lista_tipo_entidade()

@app.put('/tipo_entidade/{id}', tags=['Tipos de entidade'])
def atualiza_tipo_entidade(tipo_entidade: TipoEntidadeModel, id) -> TipoEntidadeModel:
    return tipo_entidade_controller.atualiza_tipo_entidade(tipo_entidade, id)

@app.delete('/tipo_entidade/{id}', tags=['Tipos de entidade'])
def deleta_tipo_entidade(id) -> None:
    return tipo_entidade_controller.deleta_tipo_entidade(id)


# Endpoints de entidade
@app.post('/entidade', tags=['Entidades'])
def cria_entidade(entidade: EntidadeModel) -> EntidadeSchema:
    return entidade_controller.cria_entidade(entidade)

@app.get('/entidade/{id}', tags=['Entidades'])
def obtem_entidade(id) -> EntidadeSchema:
    return entidade_controller.obtem_entidade(id)

@app.get('/entidade', tags=['Entidades'])
def lista_entidade() -> list[EntidadeSchema]:
    return entidade_controller.lista_entidade()

@app.put('/entidade/{id}', tags=['Entidades'])
def atualiza_entidade(entidade: EntidadeModel, id) -> EntidadeSchema:
    return entidade_controller.atualiza_entidade(entidade, id)

@app.delete('/entidade/{id}', tags=['Entidades'])
def deleta_entidade(id) -> None:
    return entidade_controller.deleta_entidade(id)


# Endpoints de tipo de artefatos
@app.post('/tipo_artefato', tags=['Tipos de artefato'])
def cria_tipo_artefato(entidade: TipoArtefatoModel) -> TipoArtefatoModel:
    return tipo_artefato_controller.cria_tipo_artefato(entidade)

@app.get('/tipo_artefato/{id}', tags=['Tipos de artefato'])
def obtem_tipo_artefato(id) -> TipoArtefatoModel:
    return tipo_artefato_controller.obtem_tipo_artefato(id)

@app.get('/tipo_artefato', tags=['Tipos de artefato'])
def lista_tipo_artefato() -> TipoArtefatoModel:
    return tipo_artefato_controller.lista_tipo_artefato()

@app.put('/tipo_artefato/{id}', tags=['Tipos de artefato'])
def atualiza_tipo_artefato(entidade: TipoArtefatoModel, id) -> TipoArtefatoModel:
    return tipo_artefato_controller.atualiza_tipo_artefato(entidade, id)

@app.delete('/tipo_artefato/{id}', tags=['Tipos de artefato'])
def deleta_tipo_artefato(id) -> None:
    return tipo_artefato_controller.deleta_tipo_artefato(id)


# Endpoints de artefato
@app.post('/artefato', tags=['Artefatos'])
def cria_artefato(artefato: ArtefatoModel) -> ArtefatoSchema:
    return artefato_controller.cria_artefato(artefato)

@app.get('/artefato/{id}', tags=['Artefatos'])
def obtem_artefato(id) -> ArtefatoSchema:
    return artefato_controller.obtem_artefato(id)

@app.get('/artefato', tags=['Artefatos'])
def lista_artefato() -> list[ArtefatoSchema]:
    return artefato_controller.lista_artefato()

@app.put('/artefato/{id}', tags=['Artefatos'])
def atualiza_artefato(artefato: ArtefatoModel, id) -> ArtefatoSchema:
    return artefato_controller.atualiza_artefato(artefato, id)

@app.delete('/artefato/{id}', tags=['Artefatos'])
def deleta_artefato(id) -> None:
    return artefato_controller.deleta_artefato(id)


# Endpoints de evento
@app.post('/evento', tags=['Eventos'])
def cria_evento(artefato: EventoModel) -> EventoSchema:
    return evento_controller.cria_evento(artefato)

@app.get('/evento/{id}', tags=['Eventos'])
def obtem_evento(id) -> EventoSchema:
    return evento_controller.obtem_evento(id)

@app.get('/evento', tags=['Eventos'])
def lista_evento() -> list[EventoSchema]:
    return evento_controller.lista_evento()

@app.put('/evento/{id}', tags=['Eventos'])
def atualiza_evento(artefato: EventoModel, id) -> EventoSchema:
    return evento_controller.atualiza_evento(artefato, id)

@app.delete('/evento/{id}', tags=['Eventos'])
def deleta_evento(id) -> None:
    return evento_controller.deleta_evento(id)
