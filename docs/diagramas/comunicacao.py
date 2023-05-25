import diagrams as d
import diagrams.programming.language as pl
import diagrams.programming.framework as pf
import diagrams.onprem.queue as oq
import diagrams.onprem.database as od


with d.Diagram('', filename='comunicação_entre_serviços', graph_attr={'margin': '-1.5, -1.5'}):
    api = pf.FastAPI('API')
    bd = od.PostgreSQL('Banco do dados')
    artefato = pl.Python('Artefato')
    rabbitmq = oq.RabbitMQ('Mensageria')
    aplicativo = pf.Flutter('Aplicativo')

    api >> [artefato, bd]
    api >> d.Edge(reverse=True) >> aplicativo
    artefato >> rabbitmq >> api