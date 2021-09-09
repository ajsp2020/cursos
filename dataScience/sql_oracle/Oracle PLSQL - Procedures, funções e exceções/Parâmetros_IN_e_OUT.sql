
SELECT * FROM cliente;

SELECT SUBSTR(CNPJ,1,3) || '/' || SUBSTR(CNPJ,4,2) FROM cliente;

CREATE OR REPLACE PROCEDURE formata_cnpj
(p_cnpj IN cliente.cnpj%type, p_cnpj_saida OUT cliente.cnpj%type)

-- do tipo out diz que essa variável pode sair da procedure o seu valor.

IS


BEGIN
    
    p_cnpj_saida := SUBSTR(p_cnpj,1,3) || '/' || SUBSTR(p_cnpj,4,2);

END;


-- Testando a procedure:

VARIABLE g_cnpj VARCHAR2(10)
VARIABLE g_cnpj_saida VARCHAR2(10)

EXECUTE :g_cnpj := '12345'

PRINT :g_cnpj

EXECUTE formata_cnpj(:g_cnpj, :g_cnpj_saida)

PRINT :g_cnpj
PRINT :g_cnpj_saida

