from os import getenv

from pika import PlainCredentials, ConnectionParameters, BlockingConnection


class RabbitMqConector:
    def __init__(self):
        self.usuario = getenv('RABBITMQ_USUARIO')
        self.senha = getenv('RABBITMQ_SENHA')
        self.host = getenv('RABBITMQ_HOST')
        self.porta = getenv('RABBITMQ_PORT')
        self.host_virtual = getenv('RABBITMQ_VIRTUAL_HOST')

    def abre_canal(self, nome_exchange, nome_fila='', conecta_amq_topic=False):
        # Prepara os parâmetros de conexão com a Exchange
        credenciais = PlainCredentials(self.usuario, self.senha)
        parametros = ConnectionParameters(host=self.host,
                                          port=self.porta,
                                          virtual_host=self.host_virtual,
                                          credentials=credenciais)
        conexao = BlockingConnection(parametros)  # Abre uma conexão
        canal = conexao.channel()  # Abre um canal

        # Declara a exchange, para que a mesma seja criada caso não
        # exista
        canal.exchange_declare(exchange=nome_exchange,
                               exchange_type='fanout')

        # Declara a fila, para que a mesma seja criada caso não exista
        fila_declarada = canal.queue_declare(queue=nome_fila,
                                             exclusive=True)

        # Obtém o nome "real" da fila declarada
        nome_fila_declarada = fila_declarada.method.queue

        if conecta_amq_topic:
            # Conecta no exchange amq.topic, usado pelo MQTT
            canal.exchange_bind(destination=nome_exchange,
                                source='amq.topic')

        # Conecta a fila na exchange
        canal.queue_bind(exchange=nome_exchange, queue=nome_fila_declarada)

        return canal, nome_fila_declarada
