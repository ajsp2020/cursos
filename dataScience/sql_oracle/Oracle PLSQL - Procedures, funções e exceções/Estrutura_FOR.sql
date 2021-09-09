
select * from cliente;

declare 
     v_SEGMERCADO_ID CLIENTE.SEGMERCADO_ID%type:= 3;
begin
    for v_ID in 1..6 loop
        atualizar_cli_seg_mercado(v_ID, v_SEGMERCADO_ID);
   
    end loop;
end;