$(document).ready(function(){

    animal =["perro", "gato", "león", "lobo", "oso", "ciervo", "erizo", "zorro", "vaca", "abeja", "águila", "elefante", "rinoceronte", "serpiente", "ardilla", "ballena", "tiburón", "zorro", "buitre"]
    animal = animal.sort(() => Math.random() - 0.5)

    color = ["rojo", "verde", "azul", "amarillo", "violeta", "turquesa", "cian", "dorado", "púrpura", "fucsia", "blanco", "negro", "celeste", "rosa"]
    color = color.sort(() => Math.random() - 0.5)

    fruit = ["aguacate", "manzana", "plátano", "melocotón", "kiwi", "frambuesa", "arándano", "mandarina", "pomelo", "fresa", "melón", "sandía", "limón", "coco", "piña", "mango", "dátil", "cereza"]
    fruit = fruit.sort(() => Math.random() - 0.5)

    a = animal.slice(0, 10)
    a.push(...color.slice(0,5), ...fruit.slice(0,6))
    a = a.sort(() => Math.random() - 0.5)

    c = color.slice(0, 10)
    c.push(...animal.slice(0,6), ...fruit.slice(0,5))
    c = c.sort(() => Math.random() - 0.5)
    
    f = fruit.slice(0, 10)
    f.push(...color.slice(0,5), ...animal.slice(0,6))
    f = f.sort(() => Math.random() - 0.5)

   
    animales = document.getElementsByName("animal")

    for (let index = 0; index < animales.length; index++) {
        const element = animales[index];

        element.innerHTML = a[index]
        
    }

    colores = document.getElementsByName("color")

    for (let index = 0; index < colores.length; index++) {
        const element = colores[index];

        element.innerHTML = c[index]
        
    }

    frutas = document.getElementsByName("fruta")

    for (let index = 0; index < frutas.length; index++) {
        const element = frutas[index];

        element.innerHTML = f[index]
        
    }

}); 


function setAnimal(value){

    answer = value.innerHTML
    value.style.background = "#81D3D4"
    value.disabled = true

    if(animal.includes(answer)){

        inputAnimal = document.getElementById("animals")
        inputAnimal.value = inputAnimal.value != "" ? (parseInt(inputAnimal.value)  + 1) : 1 


    }


}

function setColor(value){

    answer = value.innerHTML
    value.style.background = "#81D3D4"
    value.disabled = true

    if(color.includes(answer)){

        inputColor = document.getElementById("colors")
        inputColor.value = inputColor.value != "" ? (parseInt(inputColor.value)  + 1) : 1 
    }
    

}

function setFruta(value){

    answer = value.innerHTML
    value.style.background = "#81D3D4"
    value.disabled = true
   
    if(fruit.includes(answer)){
        console.log("jiowefhjwoiefhjowihef")
        inputFrutas = document.getElementById("frutas")
        inputFrutas.value = inputFrutas.value != "" ? (parseInt(inputFrutas.value)  + 1) : 1 
    }

}

function reset(value){

    elements = document.getElementsByName(value.id)

    for (let index = 0; index < elements.length; index++) {
        const element = elements[index];
        
        element.style.background = "white"
        element.disabled = false
    }

    document.getElementById(value.id + "s").value = ""
}

