
$(document).ready(function(){

if(document.getElementById("load").innerHTML == "False"){
    var audio1 = new Audio('../../static/assets/audios/imagesorder.mp3');
    var audio2 = new Audio('../../static/assets/audios/continuar.mp3');

    audio1.play();

    setTimeout(() => {audio2.play()}, 3500)
}

});