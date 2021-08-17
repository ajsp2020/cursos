
-- Criando uma procedure com os comando abaixo:

CREATE PROCEDURE incluir_segmercado

    (p_ID IN NUMBER, p_DESCRICAO IN VARCHAR2)

IS
    -- A declaração de todas as variáveis que serão executadas no programa
BEGIN

    INSERT INTO SEGMERCADO (ID, DESCRICAO) VALUES (p_ID, UPPER(p_DESCRICAO));
    COMMIT;

END;

-- Formas de incluir elementos na tabela:

-- Forma 1:

EXECUTE INCLUIR_SEGMERCADO(3, 'Farmaceuticos');

SELECT * FROM SEGMERCADO;

-- Forma 2:

BEGIN
    INCLUIR_SEGMERCADO(4, 'Industrial');
END;






