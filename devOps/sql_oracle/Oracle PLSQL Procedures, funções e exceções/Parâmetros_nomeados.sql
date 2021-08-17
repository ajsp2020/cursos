
declare
    v_segmercado_id cliente.segmercado_id%type := 3;
    
begin
    for v_id in 1..7 loop
        atualizar_cli_seg_mercado(p_id => v_id, p_segmercado_id => v_segmercado_id);
    end loop;
end;


select * from cliente;    