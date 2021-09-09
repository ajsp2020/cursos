declare
    -- Declaração: Onde definimos qual consulta SQL esstará ssendo carregada ao Cursor
    cursor cur_cliente is select id from cliente; 
    v_segmercado_id cliente.segmercado_id%type := 2;
    
    v_id cliente.id%type; -- Preciso dessa variável para poder receber o conteúdo do cursor. 


begin
    -- Abertura: Abrimos o Cursor para percorrê-lo linha a linha;
    open cur_cliente;
    
    -- Percorre linha a linha até o seu final;
    loop 
        fetch cur_cliente into v_id;
        
        -- Testar se tterminou o cursor. 
    exit when cur_cliente%notfound;
        atualizar_cli_seg_mercado(p_id => v_id, p_segmercado_id => v_segmercado_id);
        
    end loop;
    
    -- Fechando o cursor:
    close cur_cliente;

end;


select * from cliente;