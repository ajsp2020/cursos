#include<stdio.h>
#include<stdlib.h>
#include "fogefoge.h"
#include "mapa.h"

MAPA m;
POSICAO heroi;

int acabou() {
	return 0;
}
int ehdirecao(char direcao) {
	return direcao == 'a' || direcao == 'w' || direcao == 's' || direcao == 'd';
}

void move(char direcao) {

	if (!ehdirecao(direcao)) return;

	int proximox = heroi.x;
	int proximoy = heroi.y;

	// andando com o personagem
	switch (direcao)
	{
	case ESQUERDA:
		proximoy--;
		break;
	case CIMA:
		proximox--;
		break;
	case BAIXO:
		proximox++;
		break;
	case DIREITA:
		proximoy++;
		break; 
	}

	if (!ehvalida(&m, proximox, proximoy)) return;
	if (!ehvazia(&m, proximox, proximoy)) return;

	andanomapa(&m, heroi.x, heroi.y, proximox, proximoy);
	heroi.x = proximox;
	heroi.y = proximoy;
}

int main()
{
	lemapa(&m);
	do {
		//Imprimindo o mapa
		imprimemapa(&m);
		encontramapa(&m, &heroi, HEROI); // Encontra o personagem no mapa e atualiza 

		char comando; 
		scanf(" %c", &comando); // O espeço serve para dizer que o comando termina com um enter
		move(comando);

	} while (!acabou());


	// liberando o espaço alocado
	liberamapa(&m);
}