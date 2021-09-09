
-- Na conexão padrao criada alterar os privilégios de uso

-- Inserindo um item na tabela:
INSERT INTO SEGMERCADO (ID, DESCRICAO) VALUES (1, 'Varejo');

SELECT * FROM SEGMERCADO;

DELETE FROM SEGMERCADO;

-- Usando o plsql para inserir itens dentro da tabela:

DECLARE

    v_ID NUMBER(5) := 1; 
    v_DESCRICAO VARCHAR2 (100) := 'Varejo';

BEGIN
    
    INSERT INTO SEGMERCADO (ID, DESCRICAO) VALUES (v_ID, v_DESCRICAO);
    COMMIT;

END;

