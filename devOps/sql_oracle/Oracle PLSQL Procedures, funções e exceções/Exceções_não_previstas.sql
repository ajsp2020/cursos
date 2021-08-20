select * from segmercado;

execute incluir_cliente(13,'MERCADO RRR','45677',10,90000);

create or replace PROCEDURE incluir_cliente
(p_ID IN CLIENTE.ID%type, p_RAZAO_SOCIAL in CLIENTE.RAZAO_SOCIAL%type,
p_CNPJ IN CLIENTE.CNPJ%type, p_SEGMERCADO_ID in CLIENTE.SEGMERCADO_ID%type,
p_FATURAMENTO_PREVISTO IN CLIENTE.FATURAMENTO_PREVISTO%type)

IS

    -- Criando uma variável de trabalho
    v_categoria cliente.categoria%type;
    v_cnpj cliente.cnpj%type := p_cnpj;
    e_null exception;
    pragma exception_init (e_null, -1400);


BEGIN

    formata_cnpj(v_cnpj); -- A variável entra na procedure onde é modificada
    v_categoria := categoria_cliente(p_faturamento_previsto);

    INSERT INTO CLIENTE (ID, RAZAO_SOCIAL, CNPJ, SEGMERCADO_ID, DATA_INCLUSAO, FATURAMENTO_PREVISTO, CATEGORIA)
    VALUES (p_ID, p_RAZAo_SOCIAL, v_cnpj, p_SEGMERCADO_ID, SYSDATE, p_FATURAMENTO_PREVISTO, v_categoria);
    COMMIT;

EXCEPTION   

    WHEN dup_val_on_index THEN
        RAISE_APPLICATION_ERROR(-20010, 'Cliente já cadastrado!!!');
    
    WHEN e_null THEN
        RAISE_APPLICATION_ERROR(-20015, 'A Coluna ID não pode receber valores nulos ou vazios!!!');
        
    WHEN others THEN -- Sempre tem que ser o último erro.
        RAISE_APPLICATION_ERROR(-20020, 'ERRO GENÉRICO: ' || sqlerrm());

      
END;