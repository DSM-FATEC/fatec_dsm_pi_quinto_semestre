# Importando bibliotecas externas
from fastapi import FastAPI
from dotenv import load_dotenv

# Importando classes internas
from controllers.tipo_entidade_controller import TipoEntidadeController
from conectors.banco_de_dados_conector import BancoDeDadosConector
from models.tipo_entidade_model import TipoEntidadeModel
from repositories.tipo_entidade_repository import TipoEntidadeRepository


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

# Instanciando os controllers
tipo_entidade_controller = TipoEntidadeController(tipo_entidade_repository)

# Registrando endpoint de ping
# <objeto app>.get(endpoint) -> Registra uma url que vai responder quando
#                               fizermos uma requisição GET no servidor
# Requisições GET -> São as requisições que possuem retorno (procuram algo)
@app.get('/ping')
def ping():
    return 'pong'


# <objeto app>.post(endpoint) -> Registra uma url que vai responder quando
#                                fizermos uma requisição POST no servidor
# Requisições POST -> São as requisições que enviam dados e criam algo
@app.post('/tipo_entidade')
def cria_tipo_entidade(dados: TipoEntidadeModel):
    return tipo_entidade_controller.cria_tipo_entidade(dados)

@app.get('/tipo_entidade/{id}')
def obtem_tipo_entidade(id):
    return tipo_entidade_controller.obtem_tipo_entidade(id)

@app.get('/tipo_entidade')
def lista_tipo_entidade():
    return tipo_entidade_controller.lista_tipo_entidade()
