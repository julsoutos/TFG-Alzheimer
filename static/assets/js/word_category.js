$(document).ready(function(){

    if(document.getElementById("load").innerHTML == "False"){

    
        var audio1 = new Audio('../../static/assets/audios/category.mp3');
        var audio2 = new Audio('../../static/assets/audios/continuar.mp3');

        audio1.play();
        setTimeout(() => {audio2.play()}, 4600)



    }

    if(variant == "Word Category 1"){
        title = "Herramienta de metal que se usa para apalancar y abrir"
        words = ["palanca", "pinza", "palo", "plomo"]
        words = words.sort(() => Math.random() - 0.5)
    }

    if(variant == "Word Category 2"){
        title = "Parte inferior y alargada de la mandíbula"
        words = ["lengua", "pecho", "nuca", "mentón"]
        words = words.sort(() => Math.random() - 0.5)
    }

    if(variant == "Word Category 3"){
        title = "Persona que vende y representa productos"
        words = ["camarera", "director", "comercial", "cómico"]
        words = words.sort(() => Math.random() - 0.5)
    }

    if(variant == "Word Category 4"){
        title = "Medio de transporte con trenes bajo tierra"
        words = ["submarino", "puerto", "carro", "metro"]
        words = words.sort(() => Math.random() - 0.5)
    }





    document.getElementById("sentence").innerHTML = title
    solutions = document.getElementById("solutions")

    for (let index = 0; index < words.length; index++) {
        const element = words[index];
        
        
        var button = document.createElement("button")
                        solutions.appendChild(button)
                        button.innerHTML = element
                        button.setAttribute("name", "word")
                        button.setAttribute("type", "button")
                        button.onclick = function() { add( this )}
                        button.className = "btn btn-outline-primary category-words"


       
    }
 
}); 

function add(value){

    solutions = document.getElementsByName("word")

    for (let index = 0; index < solutions.length; index++) {
        const element = solutions[index];
        element.style.background = "#83b4e8"
        element.disabled = false
        
    }

    value.style.background = "#81D3D4"
    value.disabled = true
    document.getElementById("answer").value = value.innerHTML
    

}

function reset(){

    for (let index = 0; index < solutions.length; index++) {
        const element = solutions[index];
        element.style.background = "#83b4e8"
        element.disabled = false
        
    }

    document.getElementById("answer").value = ""
}