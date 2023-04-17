CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY NOT NULL,
    id_google VARCHAR(100) UNIQUE,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    foto TEXT,
    criado_em TIMESTAMP NOT NULL,
    atualizado_em TIMESTAMP NOT NULL
);

CREATE TABLE IF NOT EXISTS tipos_de_entidade (
    id SERIAL PRIMARY KEY NOT NULL,
    descricao VARCHAR(255) UNIQUE NOT NULL,
    criado_em TIMESTAMP NOT NULL,
    atualizado_em TIMESTAMP NOT NULL
);

CREATE TABLE IF NOT EXISTS entidades (
    id SERIAL PRIMARY KEY NOT NULL,
    tipo INTEGER NOT NULL REFERENCES tipos_de_entidade (id),
    descricao VARCHAR(255) NOT NULL,
    cep CHAR(9) NOT NULL,
    complemento VARCHAR(255),
    endereco VARCHAR(255) NOT NULL,
    bairro VARCHAR(255) NOT NULL,
    cidade VARCHAR(255) NOT NULL,
    estado VARCHAR(255) NOT NULL,
    criado_em TIMESTAMP NOT NULL,
    atualizado_em TIMESTAMP NOT NULL
);

CREATE TABLE IF NOT EXISTS tipos_de_artefato (
    id SERIAL PRIMARY KEY NOT NULL,
    descricao VARCHAR(255) UNIQUE NOT NULL,
    produtor BOOLEAN NOT NULL DEFAULT FALSE,
    criado_em TIMESTAMP NOT NULL,
    atualizado_em TIMESTAMP NOT NULL
);

CREATE TABLE IF NOT EXISTS artefatos (
    id SERIAL PRIMARY KEY NOT NULL,
    tipo INTEGER NOT NULL REFERENCES tipos_de_artefato (id),
    entidade INTEGER NOT NULL REFERENCES entidades (id),
    descricao VARCHAR(255),
    ativo BOOLEAN NOT NULL DEFAULT FALSE,
    comportamentos JSONB,
    criado_em TIMESTAMP NOT NULL,
    atualizado_em TIMESTAMP NOT NULL
);

CREATE TABLE IF NOT EXISTS eventos (
    id SERIAL PRIMARY KEY NOT NULL,
    artefato INTEGER NOT NULL REFERENCES artefatos (id),
    corpo JSONB,
    criado_em TIMESTAMP NOT NULL,
    atualizado_em TIMESTAMP NOT NULL
);
