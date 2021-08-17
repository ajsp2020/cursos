#include<stdio.h>
#include<stdlib.h>
#include "mapa.h"

void andanomapa(MAPA* m, int xorigem, int yorigem, int xdestino, int ydestino) {
	char personagem = m->matriz[xorigem][yorigem];
	m->matriz[xdestino][ydestino] = personagem;
	m->matriz[xorigem][yorigem] = VAZIO;

}

int ehvalida(MAPA* m, int x, int y) {
	if (x >= m->linhas) return 0;
	if (y >= m->colunas) return 0;
	return 1;
}

int ehvazia(MAPA* m, int x, int y) {
	return m->matriz[x][y] == VAZIO;
}

void encontramapa(MAPA* m, POSICAO* p, char c) { // Buscando a posiçaõ do personagem e guardando numa variável global
	for (int i = 0; i < m->linhas; i++) {
		for (int j = 0; j < m->colunas; j++) {
			if (m->matriz[i][j] == c) {
				p->x = i;
				p->y = j;
				break;
			}
		}
	}
}


void liberamapa(MAPA* m) {
	for (int i = 0; i < m->linhas; i++) { // Posso usar a -> sempre que tiver um ponteiro de uma struct
		free(m->matriz[i]); // Libero um para cada linha 
	}
	free(m->matriz); // Libero um para o ponteiro principal 
}

void alocamapa(MAPA* m) {
	// Fazendo a alocação dinâmica de memória
	m->matriz = malloc(sizeof(char*) * m->linhas);  // criando um espaço de memória com tamanho de um inteiro (** para matriz é necessário declarar um ponteiro de ponteiro)
	for (int i = 0; i < m->linhas; i++) {
		m->matriz[i] = malloc(sizeof(char) * (m->colunas + 1));
	}
}

void lemapa(MAPA* m) {

	// Lendo o arquivo txt com o mapa
	FILE* f;
	f = fopen("mapa.txt", "r");
	if (f == 0) {
		printf("Erro na leitura do mapa\n");
		exit(1);
	}
	// Antes de ler o mapa inteiro vou pegar a primeira linha e guardar os valores na variável linha e na variável coluna
	fscanf(f, "%d" "%d", &(m->linhas), &(m->colunas));

	alocamapa(m);

	// Guardando o valor do arquivo txt numa matriz 5 x 10
	for (int i = 0; i < 5; i++) { // Lendo todas as linhas do mapa
		fscanf(f, "%s", m->matriz[i]); // guardando no matriz mapa - mapa[i] devolve um array de char -> passando a linha inteira 
	}
	// Fechando o arquivo
	fclose(f);

}
void imprimemapa(MAPA* m) {
	for (int i = 0; i < 5; i++) {
		printf("%s\n", m->matriz[i]);
	}
}