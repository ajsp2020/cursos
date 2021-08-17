declare
    -- Declara��o: Onde definimos qual consulta SQL esstar� ssendo carregada ao Cursor
    cursor cur_cliente is select id from cliente; 
    v_segmercado_id cliente.segmercado_id%type := 1;   
    
begin
     -- N�o precisa declarar a vari�vel cli_rec
    for cli_rec in cur_cliente loop
        -- p_id => variavel declarada no for.id do cur_cliente
        atualizar_cli_seg_mercado(p_id => cli_rec.id, p_segmercado_id => v_segmercado_id);
        
    end loop;

end;

select * from cliente;