import javax.swing.plaf.synth.SynthOptionPaneUI;

public class Conta { 
	private double saldo; // com private significa que o atributo não pode ser lido ou modificado 
	private int agencia;
	private int numero;
	private Cliente titular;
	private static int total; // com o static esse total não pertence mais ao objeto mas sim a classe
	
	// construtor padrão (é escondido)
	public Conta(int agencia, int numero) {
		Conta.total ++;
		System.out.println("O total de contas é " + Conta.total);
		this.agencia = agencia;
		this.numero = numero;
		System.out.println("Estou criando uma conta " + this.numero);
	}
	
	public void deposita(double valor) {
		this.saldo += valor;
	}
	
	public boolean saca(double valor) {
		if(this.saldo >= valor) {
			this.saldo -= valor;
			return true;
		}else {
			return false;
		}
	}
	public boolean transfere(double valor, Conta destino) {
		if(this.saldo >= valor) {
			this.saldo -= valor;
			destino.deposita(valor);
			return true;
		}
		return false;
		
	}
	
	public double getSaldo() {
		return this.saldo;
	}
	
	public int getNumero() {
		return this.numero;
	}
	
	public void setNumero(int numero) {
		if(numero <= 0) {
			System.out.println("Não pode valores negativos ou zero");
			return;
		}
		this.numero = numero;
	}
	
	public int getAgencia() {
		return this.agencia; //this referece ao atributo
	}
	public void setAgencia(int agencia) {
		if(agencia <= 0) {
			System.out.println("Não pode valor menor ou igual a zero");
			return;
		}
		this.agencia = agencia;
	}
	
	public void setTitular(Cliente titular) {
		this.titular = titular;
	}
	
	public Cliente getTitular() {
		return titular;
	}
	
	public static int getTotal() { // static serve para referenciar a classe
		return Conta.total;
	}
}
