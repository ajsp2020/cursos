#include<iostream>
#include<string>

using namespace std;

struct Conta
{
    string numero;
    string cpfTitular;
    string nomeTitular;
    float saldo;

    // Conta recebe uma referencia:
    void sacar(float valorASacar)
    {
        if(valorASacar < 0){
            cout << "Não pode sacar valor negativo" << endl;
            return;
        }
        if(valorASacar > saldo){
            cout << "Saldo insuficiente" << endl;
            return;
        }

        saldo -= valorASacar;

    }

    void depositar(float valorADepositar)
{
    if(valorADepositar < 0){
        cout << "Não pode depositar valor negativo" << endl;
        return;
    }
    saldo += valorADepositar;
}

};





int main(){

    Conta umaConta;
    umaConta.numero = "123456";
    umaConta.cpfTitular = "12.456.789-10";
    umaConta.nomeTitular = "Vinícios";
    umaConta.saldo = 100;


    Conta umaOutraConta;
    umaOutraConta.saldo = 200;

  
    umaOutraConta.sacar(200);
    umaOutraConta.depositar(300);

    cout << "Uma conta: " << umaConta.saldo << " Outra conta: " << umaOutraConta.saldo << endl;

}
