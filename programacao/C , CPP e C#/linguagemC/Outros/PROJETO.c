#define BTN 11
#define BTN_A 10
#define BTN_S 12

int contagem = 0;
int espera =0;
bool soma = true;
bool somaS = false;

int mapaDisplay[] ={ //Array com o valor em binário
	B0000, B0001, B0010, B0011, B0100, B0101, B0110,
  	B0111, B1000, B1001
};
void mostrarNumero_dezena(int numero) { //Controla o display da esquerda
   if (numero < 0) numero = 0;
  
  int mapa = mapaDisplay[numero];
  int bitAtual = B0001;

  for (int i = 4; i < 10; i++){ 
    int acender= mapa & bitAtual;
    digitalWrite(i + 2, acender);
    bitAtual = bitAtual << 1;       
  }      
}
void mostrarNumero_unidade(int numero) { //Controla o display da direita
  if (numero < 0)numero = 0;
  
  int mapa = mapaDisplay[numero];
  int bitAtual = B0001;

  for (int i = 0; i < 4; i++){ 
    int acender= mapa & bitAtual;
    digitalWrite(i + 2, acender);
    bitAtual = bitAtual << 1;       
  }     
}

void mostrarDigitos(int dezena, int unidade){ //Direciona os valores do display

  mostrarNumero_unidade(unidade);
  	delay(0);

  mostrarNumero_dezena(dezena);
	delay(200); 
}
void contar(){ //Soma, subitrai e zera a contagem
  	if (digitalRead(BTN) == 1 || contagem > 99) contagem = 0;
  if (espera == 5) {
    contagem ++;
    espera = 0;
  }
  espera ++;
    
    
  mostrarDigitos(contagem / 10, contagem % 10);  
}
void contarS(){ //Soma, subitrai e zera a contagem
  	if (digitalRead(BTN) == 1 || contagem > 99) contagem = 0;
  if (espera == 5) {
    contagem --;
    espera = 0;
  }
  espera ++;
    
    
  mostrarDigitos(contagem / 10, contagem % 10);  
}

void setup(){ //Define os pinos
	pinMode(2, OUTPUT);
  	pinMode(3, OUTPUT);
	pinMode(4, OUTPUT);
	pinMode(5, OUTPUT);
  	pinMode(6, OUTPUT);
	pinMode(7, OUTPUT);
	pinMode(8, OUTPUT);
	pinMode(9, OUTPUT);
  	pinMode(BTN, INPUT_PULLUP);
  	pinMode(BTN_S, INPUT_PULLUP);
  	pinMode(BTN_A, INPUT_PULLUP); 	
}
void loop(){ //Inicia o loop
  
  if (contagem < 0) contagem = 99;
  if(digitalRead(BTN_S) == 1) {
    soma = false;
    somaS = true;
    

   while (digitalRead(BTN_S) == 0) {}
  }
  
  if (soma == true) {
    contar();
  }
  if(digitalRead(BTN_A) == 1) {
    somaS = false;
    soma = true;

   while (digitalRead(BTN_A) == 0) {}
  }
  if (soma == false){
      contarS();
  }
}