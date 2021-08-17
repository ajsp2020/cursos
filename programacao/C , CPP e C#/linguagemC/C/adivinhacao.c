#include<stdio.h>
#include<stdlib.h>
#include<time.h>

// Ajuda definir constantes (coisas que mudam nunca)
//#define NUMERO_DE_TENTATIVAS 5


int main()
{
    // Imprime o cabecalho do nosso jogo
    printf("******************************************\n");
    printf("* Bem vindo ao nosso jogo de adivinhacao *\n");
    printf("******************************************\n");
    
    int segundos = time(0);
    srand(segundos);

    int numerogrande = rand();

    int numerosecreto = numerogrande % 100;

    int chute;
    //int ganhou = 0;
    int tentativas = 1;

    double pontos = 1000;

    //for (int i = 0; i < NUMERO_DE_TENTATIVAS; i++)
    //while (ganhou == 0)
    while (1)
    
    {
        //printf("Tentativa %d de %d\n", i+1, NUMERO_DE_TENTATIVAS);
        printf("Tentativa %d,\n", tentativas);
        printf("Qual eh o seu chute? \n");
        scanf("%d", &chute);
        printf("Seu chute foi %d\n", chute);

        if (chute < 0)
        {
            printf("Voce nao pode chutar numeros negativos!\n");
            //i--;

            continue; // para a execução desse bloco de código só que faz o for continuar indo para a próxima interação do nosso loop
        }

        int acertou = (chute == numerosecreto);
        int maior = (chute > numerosecreto); // A variável existe no escopo que foi declarada e nos escopos de dentro.
   

        if (acertou)
        {

            printf("Parabens! voce acertou\n");
            printf("Jogue novamente, voce eh um bom jogador!\n");

            //break; //Encerra a o loop e sai do for
            //ganhou = 1;
            break;
            
        }
       
        else if (maior)
        {
            printf("Seu chute foi maior que o numero segreto!\n");
        }

        else 
        {
            printf("Seu chute foi menor que o numero secreto!\n");
        }
        
        tentativas ++;

        double pontosperdidos = abs(chute - numerosecreto) / (double)2; //fazendo casting (converter uma variável em outra)
        pontos = pontos - pontosperdidos;
    }    
    printf("Fim de jogo!\n");
    printf("Voce acertou em %d tentativas\n", tentativas);
    printf("Total de ponto perdidos %.1f\n", pontos);
}