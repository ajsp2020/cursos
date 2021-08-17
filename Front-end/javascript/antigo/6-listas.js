console.log(`Trabalhando com listas`);

// const salvador = `Salvador`;
// const saoPaulo = `São Paulo`;
// const rioDeJaneiro = `Rio de Janeiro`;

const listaDeDestinos = new Array(
    `Salvador`,
    `São Paulo`,
    `Rio de Janeiro`
);

listaDeDestinos.push(`Curitiba`) // Adicionando um item na lista
console.log(listaDeDestinos);
// console.log(salvador,saoPaulo,rioDeJaneiro);

listaDeDestinos.splice(1, 1); //remover um item de uma lista (posicao e quantidade de elemento)
console.log(listaDeDestinos);
console.log(listaDeDestinos[1]);