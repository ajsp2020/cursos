var pacientes = document.querySelectorAll(".paciente");
    var tabela = document.querySelector("table");

    // coloco o event para o programa saber quem foi clicado
    tabela.addEventListener("dblclick", function(event){
        //remover um elemento pai do objeto clicado na condição que seja um td
        if(event.target.tagName == 'TD')
        {
            event.target.parentNode.classList.add("fadeOut");

            // pede para o programa esperar enquando o anterior completa de funcionar
            setTimeout(function(){
                event.target.parentNode.remove();
            }, 500)
        }

    });



