#include<stdio.h>
//  usa o & para pegar o endereço de memória
// usa a * para receber o enderço de memória

void calcula(int* c2) { // para receber um endereço de memória (aqui vai vim o endereço de memória de um inteiro) -> um ponteiro para um inteiro
	printf("calcula %d %d\n", *c2, c2); // não faz diferença o nome da variável
	(*c2)++; // precisa mudar.. pq não é uma uma variavel comum, mas sim uma que guarda o enderço de memoria -> * para pegar o conteúdo dentro do endereço de memória
	printf("calcula %d %d\n",*c2, c2);

}

int main() {
	int c = 10;

	printf("main %d %d\n", c, &c);
	calcula(&c); // Enviando o endereço de memória
	printf("main %d %d\n", c, &c);
}