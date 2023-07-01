import requests


API_HOST = 'http://localhost:8000'
API_AUTH = ('carol@carol.carol', 'carol')


def seed(endpoint='', dados={}):
    for dado in dados:
        res = requests.post(endpoint, auth=API_AUTH, json=dado)

        if res.ok:
            print(f'{endpoint} - OK')
        else:
            print(f'{endpoint} - NOT OK')
            print(res.text)


def seed_tipo_entidade():
    seed(endpoint=f'{API_HOST}/tipo_entidade',
         dados=[
             {
                 'descricao': 'Prefeitura',
             },
             {
                 'descricao': 'Shopping',
             },
             {
                 'descricao': 'Galeria',
             },
             {
                 'descricao': 'Loja',
             },
         ])


def seed_entidade():
    seed(endpoint=f'{API_HOST}/entidade',
         dados=[
             {
                 'descricao': 'Prefeitura de teste',
                 'tipo': 1,
                 'cep': '13610-509',
                 'endereco': 'Rua de teste',
                 'bairro': 'Bairro de teste',
                 'cidade': 'Cidade de teste',
                 'estado': 'SP'
             },
         ])


def seed_tipo_artefato():
    seed(endpoint=f'{API_HOST}/tipo_artefato',
         dados=[
             {
                 'descricao': 'Semaforo',
                 'produtor': True
             },
             {
                 'descricao': 'Termostato',
                 'produtor': True
             },
             {
                 'descricao': 'Comercial',
                 'produtor': True
             },
             {
                 'descricao': 'Propaganda',
                 'produtor': True
             },
         ])


def seed_artefato():
    seed(endpoint=f'{API_HOST}/artefato',
         dados=[
            {
                'tipo': 2,
                'entidade': 1,
                'descricao': 'Semaforo',
                'ativo': True,
                'comportamentos': {
                    'open_duration': 5,
                    'closed_duration': 5
                },
            },
            {
                'tipo': 2,
                'entidade': 1,
                'descricao': 'Semaforo',
                'ativo': True,
                'comportamentos': {
                    'open_duration': 30,
                    'closed_duration': 20
                },
            },
         ])


seed_tipo_entidade()
seed_entidade()
seed_tipo_artefato()
seed_artefato()