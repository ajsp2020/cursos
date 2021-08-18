package br.com.alura;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class TestaCurso {
	
	public static void main(String[] args) {
		
		Curso javaColecoes = new Curso("Dominando as coleções do java", 
				"Paulo Silveira");
		
		//List<Aula> aulas = javaColecoes.getAulas();
		
		//System.out.println(aulas);
		
		//aulas.add(new Aula("Trabalhando com ArrayList", 21));
		
		//System.out.println(aulas);
		
		javaColecoes.adiciona(new Aula("Trabalhando com ArrayList", 21));
		javaColecoes.adiciona(new Aula("Criando uma aula", 15));
		javaColecoes.adiciona(new Aula("Trabalhando com Colecoes", 12));
		
		System.out.println(javaColecoes.getAulas());
		
		
		
		List<Aula> aulasImutaveis = javaColecoes.getAulas();
		System.out.println(aulasImutaveis);
		
		
		// Ordenando a lista
		/*
		 O melhor jeito de ordenar uma unmodifiable list 
		 seguindo algum critério é nos aproveitarmos da 
		 possibilidade de poder *passar a unmodifiable 
		 list no construtor de uma ArrayList tradicional* , 
		 podendo assim utilizar o método .sort() de Collections.
		 */
		
		
		List<Aula> aulas = new ArrayList<>(aulasImutaveis);
		
		Collections.sort(aulas);
		System.out.println(aulas);
		System.out.println(javaColecoes.getTempoTotal());
		
		System.out.println(javaColecoes);
		
		
		
	}
	
	
}
