import { Conta } from "./conta.js";

export class ContaCorrente extends Conta{
    static numeroDeContas = 0;

    constructor(cliente, agencia){ 
        super(0, cliente, agencia); // Para chamar o construtor da classe pai
        ContaCorrente.numeroDeContas += 1;
    }

    // Sobreescrevendo o comportamento de sacar
    sacar(valor){
        let taxa = 1.1;
        return this._sacar(valor, taxa)
        
    }
}