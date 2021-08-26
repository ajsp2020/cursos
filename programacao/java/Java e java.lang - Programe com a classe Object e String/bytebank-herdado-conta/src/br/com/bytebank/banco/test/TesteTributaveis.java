
package br.com.bytebank.banco.test;

import br.com.bytebank.banco.modelo.CalculadorDeImposto;
import br.com.bytebank.banco.modelo.ContaCorrente;
import br.com.bytebank.banco.modelo.SeguroDeVida;

/*
 * packages são diretórios que tem significado especial dentro do código fonte Java (b), 
 * a palavra chave package deve ser a primeira declaração (c) 
 * e packages servem para organização e agrupar as classes e interfaces (d). 
 * 
 * FQN (Full Qualified Name) é nome completo da classe, composto pelo nome do pacote e o nome da classe. 
 * FQN = Nome Pacote . Nome Simples da Classe
 * 
 * a) Só pode ter uma declaração package por arquivo

 * b) A declaração do import é opcional

 * c) É possível repetir a declaração import para importações de packages diferentes

 * d) A definição da classe sempre deve vir por último (após package e import)
 * 
 */
 
public class TesteTributaveis {

	public static void main(String[] args) {
		 ContaCorrente cc= new  ContaCorrente(222, 333);
		cc.deposita(100.0);
		
		 SeguroDeVida seguro = new  SeguroDeVida();
		
		 CalculadorDeImposto calc = new  CalculadorDeImposto();
		calc.registra(cc);
		calc.registra(seguro);
		
		System.out.println(calc.getTotalImposto());

	}

}
