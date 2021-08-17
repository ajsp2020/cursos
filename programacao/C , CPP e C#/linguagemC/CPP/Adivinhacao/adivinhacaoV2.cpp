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

    int acertou = 0;

    int nivel;
    printf("Qual o nível de dificuldade?\n");
    printf("(1) Facil (2) Medio (3) Dificil \n\n");
    printf("Escolha: ");
    scanf("%d", &nivel);

    int numerodetentativas;

    switch (nivel)
    {
    case 1:
        numerodetentativas = 20;
        break;
    case 2:
        numerodetentativas = 15;
        break;
    default:
        numerodetentativas = 6;
        break;
    }

    // if (nivel == 1)
    // {
    //     numerodetentativas = 20;
    // }
    // else if (nivel == 2)
    // {
    //     numerodetentativas = 15;
    // }
    // else
    // {
    //     numerodetentativas = 6;
    // }
    

    for (int i = 0; i < numerodetentativas; i++)
    {
      
        printf("Tentativa %d,\n", tentativas);
        printf("Qual eh o seu chute? \n");

        scanf("%d", &chute);
        printf("Seu chute foi %d\n", chute);

        if (chute < 0)
        {
            printf("Voce nao pode chutar numeros negativos!\n");
            continue; 
        }

        acertou = (chute == numerosecreto);
        int maior = (chute > numerosecreto); 
   

        if (acertou)
        {
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
    if(acertou)
    {
        printf("Voce ganhou!\n");
        printf("Voce acertou em %d tentativas\n", tentativas);
        printf("Total de ponto perdidos %.1f\n", pontos);
    }
    
    else
    {
        printf("Voce perdeu! Tente de novo\n");
    }
}
    
   