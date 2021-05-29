
$(document).ready(function(){
    
    path = "../../static/assets/img/figures/"

    

        types = ["triangles", "circle", "star"]
        types = types.sort(() => Math.random() - 0.5)

        initImage = getImages(path, types[0]).sort(() => Math.random() - 0.5)[0].split(",")[1]
        data = getImages(path, types[0]).sort(() => Math.random() - 0.5)

        init = document.getElementById("initImage")
        init.src = initImage


        select = document.getElementsByName("image")
        images = document.getElementsByName("loadImage")

        console.log(images)

        for (let index = 0; index < images.length; index++) {
            const element = select[index];
            var order = data[index].split(",")
            console.log(order[1] == initImage)
            console.log(initImage)

            if(order[1] == initImage){
                element.setAttribute("id", 1)

            }else{
                element.setAttribute("id", index + 2)

            }

            images[index].src = order[1]

        }



});



function getImages(path, variant){

    images = []

    for (let index = 1; index < 5; index++) {

        images.push(index + " , " + path  + variant + "/" + index + ".png")
        
    }

    return images

}

function set(value){

    solutions = document.getElementsByName("image")

    for (let index = 0; index < solutions.length; index++) {
        const element = solutions[index];
        element.style.background = "#83b4e8"
        element.disabled = false
        
    }

    value.style.background = "#81D3D4"
    value.disabled = true
    document.getElementById("answer").value = value.id

}

function reset(){
    elements = document.getElementsByName("image")
    document.getElementById("answer").value = ""

    for (let index = 0; index < elements.length; index++) {
        const element = elements[index];
        element.disabled = false
        element.style.background = "#83b4e8"
    }
}
