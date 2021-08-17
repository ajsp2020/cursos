create table TABELA_VENDEDORES (MATRICULA varchar(5), NOME varchar(100), PERCENTUAL_COMISSAO float, DATA_ADMISSAO date, 
DE_FERIAS bit);

ALTER table tabela_vendedores add primary key (MATRICULA);

insert into tabela_vendedores (matricula, nome, data_admissao, percentual_comissao, de_ferias)
values ('00235', 'Márcio Almeida Silva', '2014-08-15', 0.08, 0);

insert into tabela_vendedores (matricula, nome, data_admissao, percentual_comissao, de_ferias)
values ('00236', 'Cláudia Morais', '2013-09-17', 0.08, 1);

insert into tabela_vendedores (matricula, nome, data_admissao, percentual_comissao, de_ferias)
values ('00237', 'Roberta Martins', '2017-03-18', 0.11, 1);

insert into tabela_vendedores (matricula, nome, data_admissao, percentual_comissao, de_ferias)
values ('00238', 'Pericles Alves', '2016-08-21', 0.11, 0);

update tabela_vendedores set de_ferias = 0 where matricula = '00237';

drop table tabela_vendedores;

select * from tabela_vendedores;