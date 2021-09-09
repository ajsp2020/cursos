

DECLARE

    v_ID SEGMERCADO.ID%type := 3; -- %type serve para se houver mudanças na estrutura do banco de dados, o nosso programa não apresentará problemas
    v_DESCRICAO SEGMERCADO.DESCRICAO%type := 'Esportistas';

BEGIN
    
    INSERT INTO SEGMERCADO (ID, DESCRICAO) VALUES (v_ID, upper(v_DESCRICAO));
    COMMIT;

END;

SELECT * FROM SEGMERCADO;