-- Cria trigger que executa a função popula_timestamps() para preencher os
-- campos "criado_em" e "atualizado_em" ao criar ou atualizar dados da tabela
-- "usuarios"
CREATE OR REPLACE TRIGGER usuarios_popula_timestamps
BEFORE INSERT OR UPDATE
ON usuarios
FOR EACH ROW
EXECUTE FUNCTION popula_timestamps();

-- Cria trigger que executa a função popula_timestamps() para preencher os
-- campos "criado_em" e "atualizado_em" ao criar ou atualizar dados da tabela
-- "tipos_de_entidade"
CREATE OR REPLACE TRIGGER tipos_de_entidade_popula_timestamps
BEFORE INSERT OR UPDATE
ON tipos_de_entidade
FOR EACH ROW
EXECUTE FUNCTION popula_timestamps();

-- Cria trigger que executa a função popula_timestamps() para preencher os
-- campos "criado_em" e "atualizado_em" ao criar ou atualizar dados da tabela
-- "entidades"
CREATE OR REPLACE TRIGGER entidades_popula_timestamps
BEFORE INSERT OR UPDATE
ON entidades
FOR EACH ROW
EXECUTE FUNCTION popula_timestamps();

-- Cria trigger que executa a função popula_timestamps() para preencher os
-- campos "criado_em" e "atualizado_em" ao criar ou atualizar dados da tabela
-- "tipos_de_artefato"
CREATE OR REPLACE TRIGGER tipos_de_artefato_popula_timestamps
BEFORE INSERT OR UPDATE
ON tipos_de_artefato
FOR EACH ROW
EXECUTE FUNCTION popula_timestamps();

-- Cria trigger que executa a função popula_timestamps() para preencher os
-- campos "criado_em" e "atualizado_em" ao criar ou atualizar dados da tabela
-- "artefatos"
CREATE OR REPLACE TRIGGER artefatos_popula_timestamps
BEFORE INSERT OR UPDATE
ON artefatos
FOR EACH ROW
EXECUTE FUNCTION popula_timestamps();

-- Cria trigger que executa a função popula_timestamps() para preencher os
-- campos "criado_em" e "atualizado_em" ao criar ou atualizar dados da tabela
-- "eventos"
CREATE OR REPLACE TRIGGER eventos_popula_timestamps
BEFORE INSERT OR UPDATE
ON eventos
FOR EACH ROW
EXECUTE FUNCTION popula_timestamps();
