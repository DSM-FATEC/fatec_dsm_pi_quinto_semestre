import diagrams as d
import diagrams.aws.compute as ac
import diagrams.onprem.queue as oq

with d.Diagram('', filename='infraestrutura', graph_attr={'margin': '-1.25, -1.25'}):
    with d.Cluster('AWS'):
        lightsail_api = ac.Lightsail('API')
        lightsail_db = ac.Lightsail('Banco de dados')

    with d.Cluster('Cloud AMQP'):
        rabbitmq = oq.RabbitMQ('Mensageria')

    lightsail_api - [lightsail_db, rabbitmq]