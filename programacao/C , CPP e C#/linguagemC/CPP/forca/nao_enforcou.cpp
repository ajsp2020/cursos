#include <vector>

extern std::vector<char> chutes_errados; // Vetor de caracteres

bool nao_enforcou()
{
    return chutes_errados.size() < 5; // se for menor que 5 retorna true e mais que 5 retorna false
}