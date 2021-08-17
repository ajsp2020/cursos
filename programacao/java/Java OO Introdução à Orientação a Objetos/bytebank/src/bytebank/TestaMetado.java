package bytebank;

public class TestaMetado {
	
	public static void main(String[] args) {
		Conta conta = new Conta();
		conta.saldo = 100;
		conta.deposita(50);
		
		System.out.println(conta.saldo);
		conta.saca(20);
		System.out.println(conta.saldo);
		
		Conta conta2 = new Conta();
		conta2.deposita(1000);
		
		boolean sucessoTransferencia = conta2.transfere(3000, conta);
		
		if(sucessoTransferencia) {
			System.out.println("Transferencia realidado com sucesso");
		}else {
			System.out.println("Faltou dinheiro");
		}
		
		System.out.println(conta2.saldo);
		System.out.println(conta.saldo);
		
		conta.titular = "Antonio Pereira";
		System.out.println(conta.titular);
	}
}
