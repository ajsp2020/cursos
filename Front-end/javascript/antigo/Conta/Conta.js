// Classe abstrata -> ele só funciona para ser herdada.
export class Conta{
    
    constructor(saldoInicial, cliente, agencia){
        if(this.constructor == Conta){
            throw new Error("Você não deveria instanciar um objeto do tipo Conta Diretamente, pois essa é uma classe abstrata");
        }

        this._saldo = saldoInicial;
        this._cliente = cliente;
        this._agencia = agencia;


    }

    set cliente(novoValor){
        if(novoValor instanceof Cliente){
            this._cliente = novoValor;
        }
    }

    get cliente() {
        return this._cliente;
    }

    get saldo(){
        return this._saldo;
    }

    // Método abstrato: não é feito para ser chamado e sim sobreescrito
    sacar(valor){
        throw new Error("O método Sacar da conta é abstrato")
    }

    _sacar(valor, taxa){
        const valorSacado = taxa * valor;
        if(this._saldo >= valorSacado){
            this._saldo -= valorSacado;
            return valorSacado;
        }

        return 0;
    }

    depositar(valor){
        this._saldo += valor;
    }
    
    tranferir(valor, conta){
        const valorSacado = this.sacar(valor);
        conta.depositar(valorSacado)
    }

    
}