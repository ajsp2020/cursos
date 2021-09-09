
SET SERVEROUTPUT ON;

DECLARE
    
    v_FATURAMENTO_PREVISTO cliente.faturamento_previsto%type:= 65000;
    v_CATEGORIA cliente.categoria%type;

BEGIN

    IF v_faturamento_previsto < 10000 THEN 
    v_categoria := 'PEQUENO';
    ELSIF v_faturamento_previsto < 50000 THEN 
    v_categoria := 'MÉDIO';
    ELSIF v_faturamento_previsto < 100000 THEN 
    v_categoria := 'MÉDIO GRANDE';
    ELSE 
    v_categoria := 'GRANDE';
    END IF;
    
    DBMS_OUTPUT.put_line('A Categoria é ' || v_categoria);
    
END;