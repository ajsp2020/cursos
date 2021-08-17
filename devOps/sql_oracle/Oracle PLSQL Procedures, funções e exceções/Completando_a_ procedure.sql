create or replace NONEDITIONABLE PROCEDURE incluir_cliente
(p_ID IN CLIENTE.ID%type, p_RAZAO_SOCIAL in CLIENTE.RAZAO_SOCIAL%type,
p_CNPJ IN CLIENTE.CNPJ%type, p_SEGMERCADO_ID in CLIENTE.SEGMERCADO_ID%type,
p_FATURAMENTO_PREVISTO IN CLIENTE.FATURAMENTO_PREVISTO%type)

IS

    -- Criando uma variável de trabalho
    v_categoria cliente.categoria%type;
        
    
BEGIN

    v_categoria := categoria_cliente(p_faturamento_previsto);
    
    INSERT INTO CLIENTE (ID, RAZAO_SOCIAL, CNPJ, SEGMERCADO_ID, DATA_INCLUSAO, FATURAMENTO_PREVISTO, CATEGORIA)
    VALUES (p_ID, p_RAZAo_SOCIAL, p_CNPJ, p_SEGMERCADO_ID, SYSDATE, p_FATURAMENTO_PREVISTO, v_categoria);
    COMMIT;

END;


select * from cliente;
delete from cliente;

EXECUTE incluir_cliente(2, 'SUPERMERCADO IJK', '67890', 1, 90000);