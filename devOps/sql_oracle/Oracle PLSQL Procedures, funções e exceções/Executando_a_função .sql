
-- Chamando a fun��o:

-- FORMA 1:
-- Comando de oracle sql developer:

VARIABLE g_DESCRICAO VARCHAR2 (100)

EXECUTE : g_DESCRICAO:= obter_descricao_segmercado(1)

PRINT g_DESCRICAO

-- FORMA 2:
-- Utilizando qlsql:

SET SERVEROUTPUT ON

DECLARE

    v_DESCRICAO SEGMERCADO.DESCRICAO%type;
    
BEGIN

    v_DESCRICAO := obter_descricao_segmercado(2);
    dbms_output.put_line('A descri��o do Segmento de Mercado � ' || v_DESCRICAO);
    
END;