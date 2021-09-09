-- Criando uma função:

CREATE OR REPLACE FUNCTION obter_descricao_segmercado -- Nome da função
    (p_ID IN SEGMERCADO.ID%type) -- Passo como parâmetro
    RETURN SEGMERCADO.DESCRICAO%type --- Declaro como que é o retorno dessa função

IS -- Declarando a variável
    v_DESCRICAO SEGMERCADO.DESCRICAO%type; -- Declarando a variável de trabalho

BEGIN 
    
    -- Fazendo o select usando o into e jogando o resultado do select para a variável v_DESCRICAO
    -- E passando como parâmetro de filtro o p_ID
    SELECT DESCRICAO INTO v_DESCRICAO FROM SEGMERCADO WHERE ID = p_ID;
    RETURN v_DESCRICAO;
    
END;

-- Uma das principais características das funções é receber valores através de parâmetros e devolver um só valor, assim os parâmetros só podem ser de entrada.
-- A cláusula RETURN do cabeçalho irá indicar qual é o tipo de dado de retorno da função, ou seja, a variável do ambiente externo que receberá o valor da função também terá que ser do mesmo tipo de dado.

