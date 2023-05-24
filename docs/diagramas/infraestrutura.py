import diagrams as d
import diagrams.aws.database as ad
import diagrams.aws.compute as ac
import diagrams.onprem.queue as oq

with d.Diagram('Infraestrutura'):
    with d.Cluster('AWS'):
        lightsail = ac.Lightsail('API')
        rds = ad.RDSPostgresqlInstance('Banco de dados')

    with d.Cluster('Cloud AMQP'):
        rabbitmq = oq.RabbitMQ('Mensageria')

    lightsail - [rds, rabbitmq]