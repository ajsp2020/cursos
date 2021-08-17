package br.com.alura;

public class Aula implements Comparable<Aula>{
	
	private String titulo;
	private int tempo;
	
	public Aula(String titulo, int tempo) {
		this.titulo = titulo;
		this.tempo = tempo;
	}
	
	public int getTempo() {
		return tempo;
	}
	
	// toS...
	@Override
	public String toString() {
		// Método para imprimir valor
		return "[Aula: " + this.titulo + ", " + this.tempo + " minutos]";
	}
	
	@Override
	public int compareTo(Aula outraAula) {
		// compare os dois títulos e retorne o resultado
		return this.titulo.compareTo(outraAula.titulo);
	}
	
}
