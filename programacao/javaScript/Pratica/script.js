
var form = document.querySelector('form');
var elementoUl = document.querySelector('ul');
var input = document.getElementById('user-todo');
var buttonClear = document.getElementById('clear');
var buttonSend = document.getElementById('send');

// Addicionando valores na lista
buttonSend.addEventListener('click', (e) =>{
    e.preventDefault();
    criaLista(input.value);
    input.value = ' ';
});

var criaLista = (texto) => {
    let elementoLi = document.createElement('li');
    //elementoLi.textContent = texto;
    let input_texto = document.createTextNode(texto);
    elementoLi.appendChild(input_texto);
    elementoUl.appendChild(elementoLi);
};