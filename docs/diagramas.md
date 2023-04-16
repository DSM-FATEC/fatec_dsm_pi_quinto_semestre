# Comunicação dos artefatos

```mermaid
flowchart LR
    art1(Artefato Publisher 1)
    art2(Artefato Publisher 2)
    art3(Artefato Publisher 3)
    mob1(Mobile 1)
    mob2(Mobile 2)
    mob3(Mobile 3)
    msg(Mensageria)
    api(API)
    bd[(Banco de dados)]

    art1 --> msg
    art2 --> msg
    art3 --> msg

    msg --> api <--> bd

    api <== websocket ==> mob1
    api <== websocket ==> mob2
    api <== websocket ==> mob3
```

# Comunicação dos beacons

```mermaid
flowchart LR
    b1(Beacon 1)
    b2(Beacon 2)
    b3(Beacon 3)
    mob1(Mobile 1)
    mob2(Mobile 2)
    mob3(Mobile 3)
    api(API)
    bd[(Banco de dados)]

    mob1 <--> api
    mob2 <--> api
    mob3 <--> api
    api <--> bd

    b1 -..-> mob1
    b2 -..-> mob2
    b3 -..-> mob3
```

## Descoberta de artefatos pelo aplicativo

```mermaid
sequenceDiagram
    autonumber

    actor Usuario
    participant Aplicativo
    participant API
    participant Banco de dados

    Usuario->>Aplicativo: Abre aplicativo

    activate Usuario
    activate Aplicativo

    loop 5 Segundos
        Aplicativo-->Aplicativo: Busca por um novo artefato

        alt Novo Artefato encontrado
            Aplicativo-->Aplicativo: Obtém id do Artefato
            Aplicativo->>API: Obtém dados do Artefato pelo id

            activate API

            API->>Banco de dados: Busca dados do Artefato e seu último evento

            activate Banco de dados

            Banco de dados-->>API: Dados do Artefato e seu último evento

            deactivate Banco de dados

            alt Dados encontrados
                alt Artefato está ativo
                    API-->>Aplicativo: [200] Dados do Artefato e seu último evento
                else Artefato não está ativo
                    API-->>Aplicativo: [204] Objeto vazio
                end
            else Dados não encontrados
                API-->>Aplicativo:[204] Objeto vazio
            end

            deactivate API

            Aplicativo--)Usuario: Emite notificação sobre o Artefato

            alt Artefato é um publisher e último evento não é nulo
                Aplicativo--)Usuario: Emite notificação sobre o último evento do Artefato
            else Artefato não é publisher mas possui comportamento
                Aplicativo--)Usuario: Emite notificação sobre o comportamento do Artefato
            end
        else Artefato não encontrado
            Aplicativo-->Aplicativo: Continua
        end

    end


    deactivate Usuario
    deactivate Aplicativo
```

## Envio de eventos pelos artefatos

```mermaid
sequenceDiagram
    autonumber

    participant Artefato
    box Mensageria - RabbitMQ
        participant Topico MQTT
        participant Fila
    end
    participant API
    participant Banco de dados
    participant Aplicativo
    actor Usuario


    Artefato-)Topico MQTT: Envia id do Artefato e dados do evento

    activate Artefato
    deactivate Artefato
    activate Topico MQTT

    Topico MQTT->>Fila: Redireciona mensagem para a fila

    deactivate Topico MQTT
    activate Fila

    Fila->>API: Envia mensagem

    deactivate Fila
    activate API

    API-->API: Obtém id do Artefato pela mensagem
    API-->API: Obtém dados do evento pela mensagem

    API->>Banco de dados: Busca dados do Artefato

    activate Banco de dados

    Banco de dados-->>API: Dados do Artefato

    deactivate Banco de dados

    alt Artefato está ativo
        API-)Aplicativo: [Websocket] Envia evento

        activate Aplicativo

        Aplicativo--)Usuario: Emite notificação sobre o evento

        activate Usuario
        deactivate Usuario
        deactivate Aplicativo

        API->>Banco de dados: Salva evento no banco de dados

        activate Banco de dados

        Banco de dados-->>API: Id do evento

        deactivate Banco de dados
    else Artefato não está ativo
        API-->API: Descarta dados do evento
    end

    deactivate API

```

# Banco de dados

```mermaid
erDiagram
    users {
        serial id PK "unique, not null"
        varchar(100) google_id "unique"
        varchar(100) name "not null"
        varchar(100) email "unique, not null"
        varchar(255) password "not null"
        text picture
        timestamp created_at "default current_timestamp"
        timestamp updated_at "default current_timestamp"
    }

    artifact_types {
        serial id PK "unique, not null"
        varchar(100) description "unique, not null"
        boolean is_publisher "not null, "default false""
        timestamp created_at "default current_timestamp"
        timestamp updated_at "default current_timestamp"
    }

    artifacts {
        serial id PK "unique, not null"
        bigint type FK "not null"
        bigint entity FK "not null"
        boolean is_active "default false"
        varchar(255) description
        jsonb behavior
        timestamp created_at "default current_timestamp"
        timestamp updated_at "default current_timestamp"
    }

    events {
        serial id PK "unique, not null"
        bigint artifact_id FK "not null"
        jsonb payload
        timestamp created_at "default current_timestamp"
        timestamp updated_at "default current_timestamp"
    }

    entity_types {
        serial id PK "unique, not null"
        varchar(100) description "unique, not null"
        timestamp created_at "default current_timestamp"
        timestamp updated_at "default current_timestamp"
    }

    entities {
        serial id PK "unique, not null"
        bigint type FK "unique, not null"
        varchar(100) description "unique, not null"
        char(9) cep "not null"
        varchar(255) complement
        varchar(255) adddress "not null"
        varchar(255) neighborhood "not null"
        varchar(255) city "not null"
        varchar(255) state "not null"
        timestamp created_at "default current_timestamp"
        timestamp updated_at "default current_timestamp"
    }

    artifacts }o--|| artifact_types : "N:1"
    entities }o--|| entity_types : "N:1"
    artifacts }o--|| entities : "N:1"
    events }o--|{ artifacts : "N:N"
```
