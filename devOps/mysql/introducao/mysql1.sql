
select * from tbproduto;

select * from tbproduto where PRECO_LISTA between 16.007 and 16.009;
select * from tbproduto where PRECO_LISTA >= 16.007 and PRECO_LISTA <= 16.009;

select * from tbcliente where idade >= 18 and idade <= 22 and sexo = 'M';

select * from tbcliente where cidade = 'Rio de Janeiro' or BAIRRO = 'Jardins';

select * from tbcliente where (idade >= 18 and idade <= 22 and sexo = 'M') or (cidade = 'Rio de Janeiro' or BAIRRO = 'Jardins');

select * from tabela_vendedores;

select * from tabela_vendedores where DE_FERIAS = 1 and year(data_admissao) < 2016;