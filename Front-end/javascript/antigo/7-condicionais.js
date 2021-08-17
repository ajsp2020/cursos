console.log(`Trabalhando com condicionais`);

const listaDeDestinos = new Array(
    `Salvador`,
    `São Paulo`,
    `Rio de Janeiro`
);

const idadeComprador = 15;
const estaAcompanhada = false;
const temPassagemComprada = true;

console.log("Destinos possíveis");
console.log(listaDeDestinos);

// if (idadeComprador >= 18) {
//     console.log("Comprador maior de idade");
//     listaDeDestinos.splice(1, 1); // removendo um item
// }
// // A pessoa é menor de idade
// else if (estaAcompanhada == true) {
//     console.log("Comprador esta acompanhado");
//     listaDeDestinos.splice(1, 1); // removendo um item
// }
// else {
//     console.log("Não é maior de idade e não posso vender")
// }

if (idadeComprador >= 18 || estaAcompanhada == true) {
    console.log("Boa viagem\n");
    listaDeDestinos.splice(1, 1); // removendo um item
}
else {
    console.log("Não é maior de idade e não posso vender\n")
}

console.log("Embarque: \n\n")

if(idadeComprador >= 18 && temPassagemComprada){
    console.log("Boa viagem\n")
}
else{
    console.log("Voce não pode embarcar\n")
}

console.log(listaDeDestinos);


