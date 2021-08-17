use sucos;

alter table tbproduto add primary key (PRODUTO);

select * from tbproduto;

insert into tbproduto (
PRODUTO, NOME, EMBALAGEM, TAMANHO, SABOR, PRECO_LISTA) values (
'1040107', 'Light - 350 ml - Melância', 'Lata', '350 ml', 'Melância', 4.56);