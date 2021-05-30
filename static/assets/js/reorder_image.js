
$(document).ready(function(){
    
    path = "../../static/assets/img/reorder/"

        types = ["cat", "husky"]
        types = types.sort(() => Math.random() - 0.5)
        data  = shuffle(types[0])


    elements = document.getElementsByName("image")
    images = document.getElementsByName("imagen")
    nums = document.getElementsByName("num")

    for (let index = 0; index < 7; index++) {
        var order = data[index].split(",")
        const element = elements[index];
        const image = images[index];
        const num = nums[index]

        num.setAttribute("id", "num"+order[0].trim())
        element.setAttribute("id", order[0].trim())
        image.src = order[1].trim()
    }


});



function getImages(path, variant){

    images = []

    for (let index = 1; index < 7; index++) {

        images.push(index + " , " + path  + variant + "/" + index + ".png")
        
    }

    return images

}

function shuffle(variant){

    activityImages = getImages(path, variant)
    initialSolution = getImages(path, variant)
   
    while (equals(activityImages, initialSolution)) {
       
        activityImages = activityImages.sort(() => Math.random() - 0.5)
       
    }

   return activityImages

}

function set(value){
    num = document.getElementById("num" + value.id)
    answer = document.getElementById("answer")
    value.disabled = true   
    
    num.innerHTML = getSelected()
    answer.value = answer.value + value.id

}

function equals(a, b){
    res = true
    for (let index = 0; index < a.length; index++) {
        const elementA = a[index];
        const elementB = b[index];

        if(elementA != elementB){
            return false
        }


    }

    return res

}

function getSelected(){

    count = 0

    selected = document.getElementsByName("image")

    for (let index = 0; index < selected.length; index++) {
        const element = selected[index];
        if(element.disabled){
            count = count + 1
        }
    }

    return count


}

function reset(){
    selected = document.getElementsByName("image")
    nums = document.getElementsByName("num")

    for (let index = 0; index < selected.length; index++) {
        const element = selected[index];
        const num = nums[index]

        num.innerHTML = ""
        element.disabled = false
       
    }
    answer = document.getElementById("answer")
    answer.value = ""
}