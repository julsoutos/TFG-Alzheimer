function add(value, type){


    if(type == "addedPatient" || type == "addedActivity" || type == "addedTest" ){

          

            value.disabled = true

                var fila = document.createElement("tr");
                fila.setAttribute("id", "added " + value.id)
                var head1 = document.createElement("th")
                head1.setAttribute("scope", "row")

                if(type == "addedPatient"){

                    head1.setAttribute("name",  "patient")

                }

                if(type == "addedActivity"){

                    head1.setAttribute("name", "activity")

                }

                if( type == "addedTest"){

                    head1.setAttribute("name", "test")

                }


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

                if(type == "addedPatient"){

                    value.innerHTML = "Paciente Añadido"
                    addedPatients()
                }
    
                if(type == "addedActivity"){
    
                    value.innerHTML = "Actividad Añadida"
                    addedActivities()
                }
                
                if(type == 'addedTest'){
                    value.innerHTML = "Test Añadido"
                    addedTests()
                }
    }   


}

function del(added, element){

    document.getElementById(added).remove()

    document.getElementById(element).disabled = false
    document.getElementById(element).innerHTML = "Añadir"
    
}


function send(){
    
    inputPatients = document.getElementById("id_inputPatients")
    inputActivities = document.getElementById("id_inputActivities")
    inputTests = document.getElementById("id_inputTests")

    patients = document.getElementsByName("patient")
    activities = document.getElementsByName("activity")
    tests = document.getElementsByName("test")

    for (let index = 0; index < patients.length; index++) {

        inputPatients.value =   inputPatients.value == ""? patients[index].innerHTML : inputPatients.value  + ","  +  patients[index].innerHTML

    }

    for (let index = 0; index < activities.length; index++) {
    
        inputActivities.value  = inputActivities.value == ""? activities[index].innerHTML : inputActivities.value  + ","  +  activities[index].innerHTML
        
    }

    for (let index = 0; index < tests.length; index++) {
    
        inputTests.value  = inputTests.value == ""? tests[index].innerHTML : inputTests.value  + ","  +  tests[index].innerHTML
        
    }

}

function addedActivities(){
 document.getElementById("totalActivities").innerHTML =  document.getElementsByName("activity").length
}

function addedPatients(){
    document.getElementById("totalPatients").innerHTML =  document.getElementsByName("patient").length

}

function addedTests(){
    document.getElementById("totalTests").innerHTML =  document.getElementsByName("test").length

}