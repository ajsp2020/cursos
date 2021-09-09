
select * from cliente;

execute incluir_cliente('10','MERCADO PPP','40000',1,120000);

-- Sempre antes de rodar uma rotina deve se colocar o set serveroutput on
set serveroutput on;
execute incluir_cliente('1','MERCADO AAA','45677',1,90000);

create or replace PROCEDURE incluir_cliente
(p_ID IN CLIENTE.ID%type, p_RAZAO_SOCIAL in CLIENTE.RAZAO_SOCIAL%type,
p_CNPJ IN CLIENTE.CNPJ%type, p_SEGMERCADO_ID in CLIENTE.SEGMERCADO_ID%type,
p_FATURAMENTO_PREVISTO IN CLIENTE.FATURAMENTO_PREVISTO%type)

IS

    -- Criando uma variável de trabalho
    v_categoria cliente.categoria%type;
    v_cnpj cliente.cnpj%type := p_cnpj;


BEGIN

    formata_cnpj(v_cnpj); -- A variável entra na procedure onde é modificada
    v_categoria := categoria_cliente(p_faturamento_previsto);

    INSERT INTO CLIENTE (ID, RAZAO_SOCIAL, CNPJ, SEGMERCADO_ID, DATA_INCLUSAO, FATURAMENTO_PREVISTO, CATEGORIA)
    VALUES (p_ID, p_RAZAo_SOCIAL, v_cnpj, p_SEGMERCADO_ID, SYSDATE, p_FATURAMENTO_PREVISTO, v_categoria);
    COMMIT;

EXCEPTION   

    WHEN dup_val_on_index THEN
        DBMS_OUTPUT.PUT_LINE('CLIENTE JÁ CADASTRADO!!!!');
    
END;