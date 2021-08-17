// https://cursos.alura.com.br/data-attributes-do-html5-c109 (Datta-Attributes)

const criarTarefa = (evento) => {

    evento.preventDefault() // O formulario tem com tendencia mandar os dados para algum lugar. 
                             //com esse método estamos impedindo que isso aoconteça

    const input = document.querySelector('[data-form-input]')
    const valor = input.value
    console.log( valor )    
    input.value = ""
}

const novaTarefa = document.querySelector('[data-form-button]')

// Criando um escutador (elementos {Evento / Elemento que recebe o evento / O que vai acontecer quando o evento disparar})
novaTarefa.addEventListener('click', criarTarefa)

