-- Criando uma fun��o:

CREATE OR REPLACE FUNCTION obter_descricao_segmercado -- Nome da fun��o
    (p_ID IN SEGMERCADO.ID%type) -- Passo como par�metro
    RETURN SEGMERCADO.DESCRICAO%type --- Declaro como que � o retorno dessa fun��o

IS -- Declarando a vari�vel
    v_DESCRICAO SEGMERCADO.DESCRICAO%type; -- Declarando a vari�vel de trabalho

BEGIN 
    
    -- Fazendo o select usando o into e jogando o resultado do select para a vari�vel v_DESCRICAO
    -- E passando como par�metro de filtro o p_ID
    SELECT DESCRICAO INTO v_DESCRICAO FROM SEGMERCADO WHERE ID = p_ID;
    RETURN v_DESCRICAO;
    
END;

-- Uma das principais caracter�sticas das fun��es � receber valores atrav�s de par�metros e devolver um s� valor, assim os par�metros s� podem ser de entrada.
-- A cl�usula RETURN do cabe�alho ir� indicar qual � o tipo de dado de retorno da fun��o, ou seja, a vari�vel do ambiente externo que receber� o valor da fun��o tamb�m ter� que ser do mesmo tipo de dado.

