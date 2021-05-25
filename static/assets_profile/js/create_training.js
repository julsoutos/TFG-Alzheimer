function add(value, type){

    if(type == "addedPatient" || type == "addedActivity" ){

            if(type == "addedPatient"){

                value.innerHTML = "Paciente Añadido"

            }

            if(type == "addedActivity"){

                value.innerHTML = "Actividad Añadida"

            }

            value.disabled = true

                var fila = document.createElement("tr");
                fila.setAttribute("id", "added " + value.id)
                var head1 = document.createElement("th")
                head1.setAttribute("scope", "row")
                head1.setAttribute("name", type == "addedPatient" ? "patient" : "activity")
                head1.innerHTML = value.id
                fila.appendChild(head1);

                var td = document.createElement("td")
                var button = document.createElement("button")
                td.appendChild(button)
                button.innerHTML = "Eliminar"
                button.setAttribute("type", "button")
                button.onclick = function() { del( "added " + value.id, value.id); }
                button.className = "btn btn-outline-primary"
                fila.appendChild(td)


                document.getElementById(type).appendChild(fila)
                
    }   


}

function del(added, element){

    document.getElementById(added).remove()

    document.getElementById(element).disabled = false
    document.getElementById(element).innerHTML = "Añadir"
    
}


function send(){
    
    inputPatients = document.getElementById("inputPatients")
    inputActivities = document.getElementById("inputActivities")

    patients = document.getElementsByName("patient")
    activities = document.getElementsByName("activity")

    for (let index = 0; index < patients.length; index++) {

        inputPatients.value =   inputPatients.value == ""? patients[index].innerHTML : inputPatients.value  + ","  +  patients[index].innerHTML

    }

    for (let index = 0; index < activities.length; index++) {
    
        inputActivities.value  = inputActivities.value == ""? activities[index].innerHTML : inputActivities.value  + ","  +  activities[index].innerHTML
        
    }

}