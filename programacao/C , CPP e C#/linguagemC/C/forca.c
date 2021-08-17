#include<stdio.h>
#include<string.h>

void abertura()
{
    printf("********************************************\n");
    printf("*****         JOGO DE FORCA            *****\n");
    printf("********************************************\n\n");
}

    // int* é um ponteiro que guarda um endereço de memória
void chuta(char chutes[26], int* tentativas)
{
        char chute;
        scanf(" %c", &chute);
        // colocar um espaço antes do %c para fazer o programa ignorar o enter

        chutes[(*tentativas)] = chute;
        (*tentativas)++;
}

// o void diz qual variável a função devolve.       
int jachutou(char letra, char chutes[26], int tentativas)
{
    
            int achou = 0;

            //printf("Estou vendo a letra secreta %d %c\n",i ,  palavasecreta[i]);

            for (int j = 0; j < tentativas; j++) 
            {
                //printf("-> Chute %d %c\n",j, chutes[j]);
                if(chutes[j] == letra) 
                {
                    //printf("---> chute correto!\n");
                    achou = 1;
                    break;

                }

            }
        return achou;
}

int main() 
{
    char palavasecreta[20];

    sprintf(palavasecreta, "MELANCIA");


    int acertou = 0;
    int enforcou = 0;
    int tamanho = strlen(palavasecreta);

    char chutes[26];
    int tentativas = 0;

    // abertura
    abertura();
    
// o do -> while executa primeiro o bloco e depois checa a condição . o while primeiro checa a condição e depois executa o bloco
// a exclamação ! inverte a variável booleana.

    do 
    {

        for(int i = 0; i < tamanho; i++)
        {
                
            //aqui estava o código
            int achou = jachutou(palavasecreta[i], chutes, tentativas);

            
            if(achou)
            {
                printf("%c", palavasecreta[i]);
            }
            else
            {
                 printf("_ ");
            }

        }
        printf("\nQual letra?\n");

        // & da o indereço de memória que uma variável está guardada.
        chuta(chutes, &tentativas);
        


    } while (!acertou && !enforcou);
    
}
