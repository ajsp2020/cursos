

SET SERVEROUT ON

DECLARE 
    
    v_ID SEGMERCADO.ID%type:=1; -- C�digo que estou passando para meu plsql para ele me passar o descritor
    v_DESCRICAO SEGMERCADO.DESCRICAO%type; -- Vari�vel que vai receber o valor da descri��o
    
BEGIN

    SELECT DESCRICAO INTO v_DESCRICAO FROM SEGMERCADO WHERE ID = v_ID;
    dbms_output.put_line(v_DESCRICAO);

END;

