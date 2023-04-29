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
from conectors.banco_de_dados_conector import BancoDeDadosConector
from exceptions.registro_nao_encontrado import RegistroNaoEncontradoException
from models.tipo_entidade_model import TipoEntidadeModel
from models.entidade_model import EntidadeModel
from models.tipo_artefato_model import TipoArtefatoModel
from models.artefato_model import ArtefatoModel, ArtefatoSchema
from repositories.tipo_entidade_repository import TipoEntidadeRepository
from repositories.entidade_repository import EntidadeRepository
from repositories.tipo_artefato_repository import TipoArtefatoRepository
from repositories.artefato_repository import ArtefatoRepository


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

# Instanciando os controllers
tipo_entidade_controller = TipoEntidadeController(tipo_entidade_repository)
entidade_controller = EntidadeController(entidade_repository)
tipo_artefato_controller = TipoArtefatoController(tipo_artefato_repository)
artefato_controller = ArtefatoController(artefato_repository)


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
@app.get('/ping')
def ping():
    return 'pong'


# Endpoints de tipos de entidade
@app.post('/tipo_entidade')
def cria_tipo_entidade(tipo_entidade: TipoEntidadeModel):
    return tipo_entidade_controller.cria_tipo_entidade(tipo_entidade)

@app.get('/tipo_entidade/{id}')
def obtem_tipo_entidade(id):
    return tipo_entidade_controller.obtem_tipo_entidade(id)

@app.get('/tipo_entidade')
def lista_tipo_entidade():
    return tipo_entidade_controller.lista_tipo_entidade()

@app.put('/tipo_entidade/{id}')
def atualiza_tipo_entidade(tipo_entidade: TipoEntidadeModel, id):
    return tipo_entidade_controller.atualiza_tipo_entidade(tipo_entidade, id)

@app.delete('/tipo_entidade/{id}')
def deleta_tipo_entidade(id):
    return tipo_entidade_controller.deleta_tipo_entidade(id)


# Endpoints de entidade
@app.post('/entidade')
def cria_entidade(entidade: EntidadeModel):
    return entidade_controller.cria_entidade(entidade)

@app.get('/entidade/{id}')
def obtem_entidade(id):
    return entidade_controller.obtem_entidade(id)

@app.get('/entidade')
def lista_entidade():
    return entidade_controller.lista_entidade()

@app.put('/entidade/{id}')
def atualiza_entidade(entidade: EntidadeModel, id):
    return entidade_controller.atualiza_entidade(entidade, id)

@app.delete('/entidade/{id}')
def deleta_entidade(id):
    return entidade_controller.deleta_entidade(id)


# Endpoints de tipo de artefatos
@app.post('/tipo_artefato')
def cria_tipo_artefato(entidade: TipoArtefatoModel):
    return tipo_artefato_controller.cria_tipo_artefato(entidade)

@app.get('/tipo_artefato/{id}')
def obtem_tipo_artefato(id):
    return tipo_artefato_controller.obtem_tipo_artefato(id)

@app.get('/tipo_artefato')
def lista_tipo_artefato():
    return tipo_artefato_controller.lista_tipo_artefato()

@app.put('/tipo_artefato/{id}')
def atualiza_tipo_artefato(entidade: TipoArtefatoModel, id):
    return tipo_artefato_controller.atualiza_tipo_artefato(entidade, id)

@app.delete('/tipo_artefato/{id}')
def deleta_tipo_artefato(id):
    return tipo_artefato_controller.deleta_tipo_artefato(id)


# Endpoints de artefato
@app.post('/artefato')
def cria_artefato(artefato: ArtefatoModel) -> ArtefatoSchema:
    return artefato_controller.cria_artefato(artefato)

@app.get('/artefato/{id}')
def obtem_artefato(id) -> ArtefatoSchema:
    return artefato_controller.obtem_artefato(id)

@app.get('/artefato')
def lista_artefato() -> list[ArtefatoSchema]:
    return artefato_controller.lista_artefato()

@app.put('/artefato/{id}')
def atualiza_artefato(artefato: ArtefatoModel, id) -> ArtefatoSchema:
    return artefato_controller.atualiza_artefato(artefato, id)

@app.delete('/artefato/{id}')
def deleta_artefato(id):
    return artefato_controller.deleta_artefato(id)
