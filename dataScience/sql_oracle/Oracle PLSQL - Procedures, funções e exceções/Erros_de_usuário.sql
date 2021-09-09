select * from cliente;

EXECUTE atualizar_cli_seg_mercado(15, 2);

create or replace NONEDITIONABLE PROCEDURE atualizar_cli_seg_mercado
(p_ID CLIENTE.ID%type, p_SEGMERCADO_ID CLIENTE.SEGMERCADO_ID%type)
IS
    
    e_CLIENTE_ID_INEXISTENTE exception; -- 1-> Criando uma variável exception
    
BEGIN
    UPDATE CLIENTE SET SEGMERCADO_ID = p_SEGMERCADO_ID -- 2-> Rodar o comando update
    WHERE ID = p_ID;
    
    IF SQL%NOTFOUND THEN -- 3-> Testar se o comando retornou ou não zero linhas
    
        RAISE e_CLIENTE_ID_INEXISTENTE; -- 4-> Se retornou zero linhas euu forço o erro e pula para o exception

    END IF;
    
    COMMIT;
    
EXCEPTION

    WHEN e_CLIENTE_ID_INEXISTENTE THEN
        RAISE_APPLICATION_ERROR(-20100, 'Cliente inexistente!!!'); -- 5-> Escreve a mensagem de erro. 
        
END;