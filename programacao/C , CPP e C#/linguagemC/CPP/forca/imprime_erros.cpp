#include <vector>
#include <iostream>

extern std::vector<char> chutes_errados; // Vetor de caracteres

void imprime_erros()
{
    std::cout << "Chutes errados: ";
    for(char letra : chutes_errados)
    {
        std::cout << letra <<" ";
    }
    std::cout << std::endl;
}


