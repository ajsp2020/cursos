var titulo = document.querySelector(".titulo");
titulo.textContent = "Aparecida Nutricionista";

// A função querySelector somente nos traz um elemento

// var pacientes = document.querySelector(".paciente");

// para selecionar todos deve se usar o querySelectorAll()
var pacientes = document.querySelectorAll(".paciente");

console.log(pacientes.length);

for (var i = 0; i < pacientes.length; i++) 
{

    paciente = pacientes[i];

    var tdPeso = paciente.querySelector(".info-peso");
    var peso = tdPeso.textContent;

    var tdAltura = paciente.querySelector(".info-altura");
    var altura = tdAltura.textContent;

    var tdImc = paciente.querySelector(".info-imc");

    var alturaEhValida = validaAtura(altura);
    var pesoEhvalido = validaPeso(peso); //true or false

    if (!validaPeso(peso)){
        pesoEhvalido = false;
        tdImc.textContent = "Peso inválido";
        // Adicionando uma nova classe que busca e modifica a classe no CSS
        paciente.classList.add("paciente-invalido");
    }
    if (!validaAtura(altura)){
        alturaEhValida = false;
        tdImc.textContent = "Altura inválida"
        //.classList contêm as classes do HTML selecionado. 
        paciente.classList.add("paciente-invalido");
    }
    console.log (pesoEhvalido && alturaEhValida);
    if (alturaEhValida && pesoEhvalido){
        var imc = calculaImc(peso, altura);
        // .toFixed() -> define quantas casa decimais colocar
        tdImc.textContent = imc
    }

}

function validaPeso(peso)
{
    if (peso >= 0 && peso <= 1000)
    {
        return true;
    }
    else
    {
        return false;
    }
}

function validaAtura(altura)
{
    if(altura >= 0 && altura <= 3.0)
    {
        return true;
    }
    else
    {
        return false;
    }
}


function calculaImc(peso, altura)
{
    var imc = 0;

    imc = peso / (altura * altura);

    return imc.toFixed(2);
}



