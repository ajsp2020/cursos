
public class TestaCondicional {

	public static void main(String[] args) {
		System.out.println("Testando condicionais");
		int idade = 10;
		int quantidadePessoas = 3;

		if (idade >= 18) {
			System.out.println("Voc� tem mais de 18 anos");
			System.out.println("Seja bem vindo");
		} else {
			if (quantidadePessoas >= 2) {
				System.out.println("Voce n�o tem 18, mas pode entrar, pois est� acompanhado");
			} else {
				System.out.println("Infelizmente voce n�o pode entrar");
			}

		}
	}
}
