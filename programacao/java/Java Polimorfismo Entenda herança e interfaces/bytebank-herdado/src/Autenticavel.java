// contrato Autenticavel
	//quem assinar esse contrato precisa implementat
		//metodo setSenha
		//metodo autentica


public abstract interface Autenticavel  { // todos os m�todos precisam ser abstratos (n�o pode nada concreto)
	
	public abstract void setSenha(int senha);
	
	public abstract boolean autentica(int senha) ;
	

}

