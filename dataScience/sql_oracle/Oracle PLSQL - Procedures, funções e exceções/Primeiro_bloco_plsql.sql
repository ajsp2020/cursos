-- Criando uma função pl sql

-- Fazendo uma declaração da variável interna antes do declare
SET SERVEROUTPUT ON;

DECLARE 
    v_ID NUMBER(5):= 1;

BEGIN
    
    v_ID := 2; -- Alterando o valor da variável
    dbms_output.put_line(v_ID); -- Imprimindo o valor da variável na saída

END;

COMMIT;