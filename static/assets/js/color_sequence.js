
$(document).ready(function(){


    if(document.getElementById("load").innerHTML == "False"){

    
        var audio1 = new Audio('../../static/assets/audios/secuencia.mp3');
        var audio2 = new Audio('../../static/assets/audios/continuar.mp3');

        audio1.play();
        setTimeout(() => {audio2.play()}, 3800)



    }


    if(document.getElementById("load").innerHTML == "True"){
        
    
    
    if(document.getElementById("variant").innerHTML == "Color Order 1"){
            colors = ["pink", "red", "yellow", "purple", "green", "blue"]
            setTimeout(() => {changeColor("1", colors[0], 1000), 
                            changeColor("6", colors[5], 3000),
                            changeColor("6", colors[5], 5000),
                            changeColor("3", colors[2], 7000)}, 1000)
        

    }

    if(document.getElementById("variant").innerHTML == "Color Order 2"){
        colors = ["red", "purple", "pink", "blue", "yellow", "green"]

        setTimeout(() => {changeColor("3", colors[2], 1000), 
                        changeColor("1", colors[0], 3000),
                        changeColor("1", colors[0], 5000),
                        changeColor("5", colors[4], 7000)}, 1000)
    
        setTimeout(() => {enableButtons()}, 11000)

    }

    if(document.getElementById("variant").innerHTML == "Color Order 3"){
        colors = ["blue", "yellow", "green", "red", "pink", "purple"]

        setTimeout(() => {changeColor("2", colors[1], 1000), 
                        changeColor("4", colors[3], 3000),
                        changeColor("5", colors[4], 5000),
                        changeColor("1", colors[0], 7000)}, 1000)
    
        setTimeout(() => {enableButtons()}, 11000)

    }  

    setTimeout(() => {enableButtons(), document.getElementById("title").innerHTML="Introduce la secuencia generada"}, 11200)
    }
  
  });

function changeColor(id, color, time) {
    setTimeout(() => {
        document.getElementById(id).style.background = color
        setTimeout(() => {    document.getElementById(id).style.background = color ,
            setTimeout(() => {    document.getElementById(id).style.background = "white"}, 300)
        }, 1000)
    }, time)
   
}

function enableButtons(){

    buttons = document.getElementsByClassName("colors")
   
    for (let index = 0; index < buttons.length; index++) {
        
        buttons[index].disabled = false
        
    }
}

function set(value){
    id = value.id
    document.getElementById(id).style.background = colors[id-1]
    setTimeout(() => {    document.getElementById(id).style.background = "white" }, 50)
    document.getElementById("answer").value = document.getElementById("answer").value != undefined ? document.getElementById("answer").value + id : id
}

