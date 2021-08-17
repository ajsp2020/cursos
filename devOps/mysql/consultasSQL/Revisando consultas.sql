use sucos_vendas;

select * from tabela_de_clientes;

select cpf, nome from tabela_de_clientes;

select cpf as indentificador, nome as cliente from tabela_de_clientes;

select * from tabela_de_produtos;

select * from tabela_de_produtos where CODIGO_DO_PRODUTO = '1000889';

select * from tabela_de_produtos where SABOR = 'Laranja';	

select * from tabela_de_produtos where EMBALAGEM = 'PET';

select * from tabela_de_produtos where EMBALAGEM = 'pet';

select * from tabela_de_produtos where PRECO_DE_LISTA = 19.51;

select * from tabela_de_produtos where PRECO_DE_LISTA between 19.49 and 19.52;