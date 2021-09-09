

DECLARE

    v_ID SEGMERCADO.ID%type := 2; -- %type serve para se houver mudanças na estrutura do banco de dados, o nosso programa não apresentará problemas
    v_DESCRICAO SEGMERCADO.DESCRICAO%type := 'Atacadistas';

BEGIN

    UPDATE SEGMERCADO SET DESCRICAO = upper(v_DESCRICAO) WHERE ID = v_ID;
    
    v_ID := 1;
    v_DESCRICAO := 'Varejistas'; 
    UPDATE SEGMERCADO SET DESCRICAO = upper(v_DESCRICAO) WHERE ID = v_ID;

    COMMIT;

END;


SELECT * FROM SEGMERCADO;