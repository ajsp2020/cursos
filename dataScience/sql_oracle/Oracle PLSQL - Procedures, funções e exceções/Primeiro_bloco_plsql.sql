-- Criando uma fun��o pl sql

-- Fazendo uma declara��o da vari�vel interna antes do declare
SET SERVEROUTPUT ON;

DECLARE 
    v_ID NUMBER(5):= 1;

BEGIN
    
    v_ID := 2; -- Alterando o valor da vari�vel
    dbms_output.put_line(v_ID); -- Imprimindo o valor da vari�vel na sa�da

END;

COMMIT;