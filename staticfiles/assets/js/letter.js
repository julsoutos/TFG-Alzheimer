$(document).ready(function(){
    


    activity = document.getElementById("activity").innerHTML    

    if(document.getElementById("load").innerHTML == "False"){

    var audio1 = new Audio('../../static/assets/audios/letter.mp3');
    var audio2 = new Audio('../../static/assets/audios/continuar.mp3');

    audio1.play();

    setTimeout(() => {audio2.play()}, 3500)
    }

    if(document.getElementById("load").innerHTML == "True"){
    variant = document.getElementById("variant").innerHTML
    
    letters = document.getElementsByName('letter')
    console.log(letters)

    list = list()

    for (let index = 0; index < list.length ; index++) {
        
        letter = letters[index] 
        letter.innerHTML = list[index]
    }

    }

});

function list() {

    let characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l' ,'m' ,'n' ,'o' ,'p', 'q' ,'r' ,'s' ,'t', 'u', 'v' ,'p' ,'w' ,'y', 'z', 'A', 'B', 'C', 'D']

    res = characters.sort(() => Math.random() - 0.5)
  
    return res;
}

function set(element){

    
    elements = document.getElementsByName("letter")
    for (let index = 0; index < elements.length; index++) {
        const l = elements[index];
        l.style.background = "white"
        l.disabled=false
    }
    console.log(element)
    element.style.background = "#81D3D4"
    element.disabled = true
    document.getElementById("answer").value = element.innerHTML   

}


function reset(){

    document.getElementById("answer").value = ""    
    letters = document.getElementsByName('letter')
    for (let index = 0; index < letters.length; index++) {
        letters[index].style.background = "white" 
        letters[index].disabled = false

    }

}