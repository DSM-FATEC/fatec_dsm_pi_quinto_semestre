-- Função que popula os campos criado_em e atualizado_em de uma tabela, deve
-- ser usanda junto de um trigger "BEFORE"
CREATE OR REPLACE FUNCTION popula_timestamps()
RETURNS TRIGGER
AS $$
    BEGIN
        IF TG_OP = 'INSERT' THEN
            NEW.criado_em := CURRENT_TIMESTAMP;
            NEW.atualizado_em := CURRENT_TIMESTAMP;
        END IF;

        IF TG_OP = 'UPDATE' THEN
            NEW.atualizado_em := CURRENT_TIMESTAMP;
        END IF;

        RETURN NEW;
    END;
$$ LANGUAGE plpgsql;
