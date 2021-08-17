
-- Substituindo a declara��o pelo percent type

CREATE OR REPLACE PROCEDURE incluir_segmercado

    (p_ID IN SEGMERCADO.ID%type, p_DESCRICAO IN SEGMERCADO.DESCRICAO%type)

IS
    -- A declara��o de todas as vari�veis que ser�o executadas no programa
BEGIN

    INSERT INTO SEGMERCADO (ID, DESCRICAO) VALUES (p_ID, UPPER(p_DESCRICAO));
    COMMIT;

END;

-- OBS: Podemos criar procedure que n�o contenha par�metros