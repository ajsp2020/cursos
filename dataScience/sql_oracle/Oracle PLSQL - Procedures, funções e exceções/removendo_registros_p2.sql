
-- Comando em sql para excluir um elemento na tabela.

DECLARE
    
    v_ID SEGMERCADO.ID%type := 3;

BEGIN

    DELETE FROM SEGMERCADO WHERE ID = 3;
    COMMIT;

END;

SELECT * FROM SEGMERCADO;