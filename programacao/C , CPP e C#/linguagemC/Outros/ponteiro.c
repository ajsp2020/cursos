#include<stdio.h>

// &QQC da indereço da memória

// quando eu uso a * estou indicando ao meu programa que no local está indo um endereço de memória. 
void calcula(int* c)
{
    // printf("calcula %d %d", c, &c);
    printf("calcula %d %d\n", (*c), c);
    // o * detro de uma variável é usado como recurso para o modificar o conteúdo tentro do endereço de memória.
    (*c)++;
    printf("calcula %d %d\n", (*c), c);

}

int main()
{
    int c = 10;
    
    printf("main %d\n",c , &c);
    //preciso colocar o indereço da memória
    calcula(&c);
    printf("main %d\n",c , &c);
}