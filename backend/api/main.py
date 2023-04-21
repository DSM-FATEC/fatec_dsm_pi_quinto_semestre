import os

# Importando bibliotecas externas
from fastapi import FastAPI
from dotenv import load_dotenv

# Importando classes internas
from controllers.tipo_entidade_controller import TipoEntidadeController
from database.conector_banco_de_dados import ConectorBancoDeDados
from models.tipo_entidade_model import TipoEntidadeModel


# Carrega o arquivo de configurações, tornando as variáveis presentes
# nele acessíveis usando os.environ ou os.getenv()
load_dotenv()

# Criando a variável global que o FastAPI vai usar como ponto de entrada
app = FastAPI()

# Conectando ao banco de dados e abrindo uma pool de conexões
conector = ConectorBancoDeDados()
pool = conector.abre_pool()

# Instanciando os controllers
tipo_entidade_controller = TipoEntidadeController()

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
