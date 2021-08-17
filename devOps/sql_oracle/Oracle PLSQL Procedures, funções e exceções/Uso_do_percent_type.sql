

-- Usando o plsql para inserir itens dentro da tabela:

DECLARE

    v_ID SEGMERCADO.ID%type := 2; -- %type serve para se houver mudanças na estrutura do banco de dados, o nosso programa não apresentará problemas
    v_DESCRICAO SEGMERCADO.DESCRICAO%type := 'Atacado';

BEGIN
    
    INSERT INTO SEGMERCADO (ID, DESCRICAO) VALUES (v_ID, v_DESCRICAO);
    COMMIT;

END;

SELECT * FROM SEGMERCADO;