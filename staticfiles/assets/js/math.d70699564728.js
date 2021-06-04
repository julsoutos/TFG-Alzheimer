 
$(document).ready(function(){
    
    if(document.getElementById("load").innerHTML == "False"){

    
        var audio1 = new Audio('../../static/assets/audios/sum.mp3');
        var audio2 = new Audio('../../static/assets/audios/continuar.mp3');

        audio1.play();
        setTimeout(() => {audio2.play()}, 3600)



    }

    if(document.getElementById("variant").innerHTML == "Math Operations 1"){
        op = [[12, 5, '+'], [15, 2, '+'], [20, 3, '-'], [23, 6, '-']]
        op = op.sort(() => Math.random() - 0.5)
        document.getElementById("operation").innerHTML = op[0][0] + op[0][2] + op[0][1]
    }

    if(document.getElementById("variant").innerHTML  == "Math Operations 2"){
        op = [[48, 3, '+'], [26, 25, '+'], [68, 17, '-'], [59, 8, '-']]
        op = op.sort(() => Math.random() - 0.5)
        document.getElementById("operation").innerHTML = op[0][0] + op[0][2] + op[0][1]
    }

    if(document.getElementById("variant").innerHTML  == "Math Operations 3"){
        op = [[11, 8, '+'], [16, 3, '+'], [29, 10, '-'], [37, 18, '-']]
        op = op.sort(() => Math.random() - 0.5)
        document.getElementById("operation").innerHTML = op[0][0] + op[0][2] + op[0][1]
    }

    sign(op)
    

});

function sign(operation){

    if (operation[0][2] == '+'){
        document.getElementById("title").innerHTML = "Realice la siguiente suma"
    }else if(operation[0][2] == '-'){
        document.getElementById("title").innerHTML = "Realice la siguiente resta"
    }

}