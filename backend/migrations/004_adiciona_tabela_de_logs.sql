-- Cria tabela
CREATE TABLE IF NOT EXISTS logs (
    id SERIAL PRIMARY KEY NOT NULL,
    nivel VARCHAR(10) NOT NULL,
    mensagem TEXT NOT NULL,
    criado_em TIMESTAMP NOT NULL,
    atualizado_em TIMESTAMP NOT NULL
);

-- Cria trigger
CREATE OR REPLACE TRIGGER logs_popula_timestamps
BEFORE INSERT OR UPDATE
ON logs
FOR EACH ROW
EXECUTE FUNCTION popula_timestamps();
