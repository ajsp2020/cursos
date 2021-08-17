#include<stdio.h>

int numero;

int main()
{
    printf("Digite um número inteiro: ");
    scanf("%d", &numero);

    for(int i=1 ; i <= 10; i++)
    {
        printf("%dx%d = %d\n",numero, i, numero * i);
    }
}