#include <iostream> // biblioteca de entrada e saída de dados
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
    
    cout <<"*************************************" <<endl;
    cout <<"* Bem-vindos ao jogo da adivinhação *" <<endl;
    cout <<"*************************************" <<endl;

    cout << "Escolha o seu nível de dificudade: " << endl;
    cout << "Fácil (F), Médio (M) ou Difícil (D)" << endl;

    char dificuldade;
    cin >> dificuldade;

    int numero_de_tentativas;

    if(dificuldade == 'F')
    {
        numero_de_tentativas = 15;
    }
    else if (dificuldade == 'M')
    {
        numero_de_tentativas = 10;
    }
    else 
    {
        numero_de_tentativas = 5;
    }

    // colocar constantes com letra maiuscula
    srand(time(NULL));
    const int NUMERO_SECRETO = rand() % 100; 
    
    bool nao_acertou  = true;
    int tentativas;
    
    double pontos = 1000.0;

    while (nao_acertou)
    {
        for (tentativas = 1; tentativas <= numero_de_tentativas; tentativas++)
        {
        
            int chute;
            cout << "Tentativa " << tentativas <<endl;
            cout << "Qual seu chute? ";
            cin >> chute;
            cout << "O valor do seu chute é: "<< chute <<endl;

            double pontos_perdidos = abs(chute - NUMERO_SECRETO)/2.0;
            pontos -= pontos_perdidos;

            bool acertou = chute == NUMERO_SECRETO;
            bool maior = chute > NUMERO_SECRETO;

            if (acertou)
            {
                cout << "Parabéns, Você acertou o número secreto!" << endl;
                nao_acertou = false;
                break;
            }
            else if (maior)
            {
                cout << "Seu chute foi maior que o número secreto!" << endl;
            }
            else
            {
                cout << "Seu chute foi menor que o número secreto!" << endl;
                
            }
        }
        break;
    }
    
    cout << "Fim de jogo!" <<endl;
    if(nao_acertou)
    {
        cout << "Você perdeu, tente novamente!" << endl;
    }
    else
    {
        cout <<"Você acertou o número secreto em " << tentativas  << " tentativas" <<endl;
        // para definir o número de casas decimais depois da vírgula. obs -> fazer antes da saída.
        cout.precision(2);
        cout << fixed;
        cout <<"Sua pontuação foi de " << pontos <<" pontos " <<endl;
    }
    

}