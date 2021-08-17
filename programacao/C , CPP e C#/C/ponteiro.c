#include<stdio.h>
//  usa o & para pegar o endere�o de mem�ria
// usa a * para receber o ender�o de mem�ria

void calcula(int* c2) { // para receber um endere�o de mem�ria (aqui vai vim o endere�o de mem�ria de um inteiro) -> um ponteiro para um inteiro
	printf("calcula %d %d\n", *c2, c2); // n�o faz diferen�a o nome da vari�vel
	(*c2)++; // precisa mudar.. pq n�o � uma uma variavel comum, mas sim uma que guarda o ender�o de memoria -> * para pegar o conte�do dentro do endere�o de mem�ria
	printf("calcula %d %d\n",*c2, c2);

}

int main() {
	int c = 10;

	printf("main %d %d\n", c, &c);
	calcula(&c); // Enviando o endere�o de mem�ria
	printf("main %d %d\n", c, &c);
}