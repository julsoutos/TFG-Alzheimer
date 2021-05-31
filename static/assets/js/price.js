
$(document).ready(function(){
    
    money = ["0.1", "0.2", "0.5" , "0.1", "1", "2", "5","10", "20", "50"]

    money  = money.sort(() => Math.random() - 0.5)
    console.log(money)

    if(document.getElementById("load").innerHTML == "False"){

    // var audio1 = new Audio('../../static/assets/audios/letter.mp3');
    

    // audio1.play();


    }



    if(document.getElementById("load").innerHTML == "True"){

        setPrices(money)
    
    }


});



function setPrices(elements){

    prices = document.getElementsByName("prices")

    for (let index = 0; index < prices.length; index++) {
        
        prices[index].innerHTML = elements[index] + "€"
        
    }

}

function set(element){  

  newValue = parseFloat(element.innerHTML)
   
  document.getElementById("money").innerHTML = document.getElementById("money").innerHTML != undefined ? (parseFloat(document.getElementById("money").innerHTML)  + newValue).toFixed(2) + "€": newValue + "€"

  console.log(document.getElementById("answer").value )
  document.getElementById("answer").value = document.getElementById("answer").value != "" ? (parseFloat(document.getElementById("answer").value)  + newValue).toFixed(2)  : newValue 


}

function reset(){

    document.getElementById("money").innerHTML = "0" + "€"
    document.getElementById("answer").value = ""

}


