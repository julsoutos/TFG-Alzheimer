$(document).ready(function(){

    
if(document.getElementById("load").innerHTML == "False"){
    var audio1 = new Audio('../../static/assets/audios/sentence.mp3');
    var audio2 = new Audio('../../static/assets/audios/continuar.mp3');

    audio1.play();

    setTimeout(() => {audio2.play()}, 3600)
}

   var initialSolution = s

   var sentence = s

   var variant = shuffle(sentence, initialSolution)

    var section = document.getElementById("solutions") 

            
    for (let index = 0; index < variant.length; index++) {
        const element = variant[index];
        

        var button = document.createElement("button")
                        section.appendChild(button)
                        button.innerHTML = element.trim()
                        button.setAttribute("name", "word")
                        button.setAttribute("type", "button")
                        button.onclick = function() { add( this )}
                        button.className = "btn btn-outline-primary order-words"



    }



}); 

function shuffle(sentence, initialSolution){


    while (sentence == initialSolution) {
       
        sentence = s.split(" ").sort(() => Math.random() - 0.5)
        sentence = sentence.join(" ")

   }

   return sentence.split(" ")

}

function add(value){
    value.disabled = true

    solutions  = document.getElementById("sentence")

    solutions.innerHTML = solutions.innerHTML + " "  + value.innerHTML

}


function reset(){
    document.getElementById("sentence").innerHTML = ""

    elements = document.getElementsByName("word")

    for (let index = 0; index < elements.length; index++) {
        const element = elements[index];
        element.disabled = false
    }
}

function send(){

    answer = document.getElementById("answer")
    solution =  document.getElementById("sentence")


    answer.value = solution.innerHTML.trim()

    
}