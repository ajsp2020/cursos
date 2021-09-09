


DECLARE

    v_ID SEGMERCADO.ID%type := 2; -- %type serve para se houver mudanças na estrutura do banco de dados, o nosso programa não apresentará problemas
    v_DESCRICAO SEGMERCADO.DESCRICAO%type := 'Atacado';

BEGIN
    
    INSERT INTO SEGMERCADO (ID, DESCRICAO) VALUES (v_ID, upper(v_DESCRICAO));
    COMMIT;

END;


SELECT * FROM SEGMERCADO WHERE DESCRICAO = 'Atacado';

SELECT * FROM SEGMERCADO WHERE DESCRICAO = 'atacado';

DELETE FROM SEGMERCADO WHERE ID = 2;

SELECT * FROM SEGMERCADO WHERE DESCRICAO = 'ATACADO';