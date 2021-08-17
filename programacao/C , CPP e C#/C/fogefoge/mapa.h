#define HEROI '@'
#define VAZIO '.'
#define PAREDE_VERTICAL '|'
#define PAREDE_HORIZONTAL '-'


struct mapa {
	char** matriz; // Matriz de 5 x 10 -> array com mais de uma dimens�o
	int linhas;
	int colunas;
};

typedef struct mapa MAPA; // Cria um apelido para o tipo

struct posicao {
	int x;
	int y;
};
typedef struct posicao POSICAO;


void liberamapa(MAPA* m);
void lemapa(MAPA* m);
void alocamapa(MAPA* m);
void imprimemapa(MAPA* m);
void encontramapa(MAPA* m, POSICAO* p, char c);
int ehvalida(MAPA* m, int x, int y);
int ehvazia(MAPA* m, int x, int y);
void andanomapa(MAPA* m, int xorigem, int yorigem, int xdestino, int ydestino);