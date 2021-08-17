

CREATE OR REPLACE FUNCTION categoria_cliente
(p_faturamento_previsto in cliente.faturamento_previsto%type)
RETURN cliente.categoria%type


IS

    v_categoria cliente.categoria%type;

BEGIN

    IF p_faturamento_previsto < 10000 THEN 
    v_categoria := 'PEQUENO';
    ELSIF p_faturamento_previsto < 50000 THEN 
    v_categoria := 'MÉDIO';
    ELSIF p_faturamento_previsto < 100000 THEN 
    v_categoria := 'MÉDIO GRANDE';
    ELSE 
    v_categoria := 'GRANDE';
    END IF;
    
    RETURN v_categoria;
    
END;

VARIABLE g_categoria VARCHAR2(100);

EXECUTE :g_categoria := categoria_cliente(110000);

print g_categoria;




