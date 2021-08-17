#include <iostream>
#include <vector>
#include <map>
#include "letra_existe.hpp"


extern std::map<char, bool> chutou; // funciona como um dicionário
extern std::vector<char> chutes_errados; // Vetor de caracteres

void chuta()
{
    std::cout << "Seu chute: ";
    char chute;
    std::cin >> chute;
    chute = toupper(chute);

    chutou[chute] = true;

    if(letra_existe(chute))
    {
        std::cout << "Você acertou! Seu chute está na palavra." << std::endl;
    }
    else
    {
        std::cout << "Você errou! Seu chute não está na palavra." << std::endl;
        chutes_errados.push_back(chute); // para inserir o caractere errado no vetor
    }
    std::cout << std::endl;
}