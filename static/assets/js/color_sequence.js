

$(document).ready(function(){

    
    if(document.getElementById("variant").innerHTML == "Color Order 1"){
            colors = ["pink", "red", "yellow", "purple", "green", "blue"]
            setTimeout(() => {changeColor("1", colors[0], 1000), 
                            changeColor("6", colors[5], 3000),
                            changeColor("6", colors[5], 5000),
                            changeColor("3", colors[2], 7000),
                            changeColor("1", colors[0], 9000)}, 1000)
        

    }

    if(document.getElementById("variant").innerHTML == "Color Order 2"){
        colors = ["red", "purple", "pink", "blue", "yellow", "green"]

        setTimeout(() => {changeColor("3", colors[2], 1000), 
                        changeColor("1", colors[0], 3000),
                        changeColor("1", colors[0], 5000),
                        changeColor("5", colors[4], 7000),
                        changeColor("2", colors[1], 9000)}, 1000)
    
        setTimeout(() => {enableButtons()}, 11000)

    }

    if(document.getElementById("variant").innerHTML == "Color Order 3"){
        colors = ["blue", "yellow", "green", "red", "pink", "purple"]

        setTimeout(() => {changeColor("2", colors[1], 1000), 
                        changeColor("4", colors[3], 3000),
                        changeColor("5", colors[4], 5000),
                        changeColor("1", colors[0], 7000),
                        changeColor("2", colors[1], 9000)}, 1000)
    
        setTimeout(() => {enableButtons()}, 11000)

    }  

    setTimeout(() => {enableButtons(), document.getElementById("title").innerHTML="Introduce la secuencia generada"}, 11200)

  
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
    setTimeout(() => {    document.getElementById(id).style.background = "white" }, 200)
    document.getElementById("answer").value = document.getElementById("answer").value != undefined ? document.getElementById("answer").value + id : id
}

function reset(){
    document.getElementById("answer").value = ""

}