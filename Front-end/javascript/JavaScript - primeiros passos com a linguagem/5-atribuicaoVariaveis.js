
console.log("5-Trabalhando com atribuição de  variáveis");

const idade = 29;
let nome = "Ricardo"; // let -> variável comum ((melhor deixar a variável constante)
const sobrenome = "Bugan";

//console.log(nome + " " + sobrenome);
console.log(nome , sobrenome);
console.log('Meu nome é ${nome}'); // não está funcionando

nome = nome + sobrenome;
const nomeCompleto = nome + sobrenome // Melhor prática
console.log(nome);