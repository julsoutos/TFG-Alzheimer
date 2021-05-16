$(document).ready(function(){
    


    activity = document.getElementById("activity").innerHTML    

    if(document.getElementById("load").innerHTML == "False"){

    var audio1 = new Audio('../../static/assets/audios/letter.mp3');
    

    audio1.play();

    setTimeout(() => {document.getElementById("continue").click()}, 5000)

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

    id = element.id
    document.getElementById(id).style.background = "#81D3D4"
    setTimeout(() => {    document.getElementById(id).style.background = "white" }, 50)
    document.getElementById("answer").value = element.innerHTML   

}

