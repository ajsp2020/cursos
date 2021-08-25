package br.com.alura.java.io.teste;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;

public class TesteLeitura {
//necessário uma vez que a exceção checked FileNotFoundException pode ser lançada pelo construtor da classe FileInputStream caso o arquivo cujo nome é informado não exista.
	public static void main(String[] args) throws IOException {
		
		//Fluxo de entrada com arquivo
		
		InputStream fis = new FileInputStream("lorem.txt"); // Criando um fluxo completo com um arquivo binário
		Reader isr = new InputStreamReader(fis); // Melhorando os dados binários para caractéres
		BufferedReader br = new BufferedReader(isr); // 
		
		
		String linha = br.readLine();
		
		while(linha != null) {
			System.out.println(linha);
			linha = br.readLine();
		}
		
		
		
		br.close();
		
		
	}

}
