function setDay(value){

    document.getElementById("sendDay").click()

}



var memoria = document.getElementById('memoria').getContext('2d');

var memoria = new Chart(memoria, {
    type: 'doughnut',
    data: {
        labels: ['Correctas', 'Incorrectas'],
        datasets: [{
            label: '# of Votes',
            data: [diary['correct_memory'], diary['incorrect_memory']],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
               
            ],
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio:false,
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});




var atencion = document.getElementById('atencion').getContext('2d');

var atencion = new Chart(atencion, {
    type: 'doughnut',
    data: {
        labels: ['Correctas', 'Incorrectas'],
        datasets: [{
            label: '# of Votes',
            data: [diary['correct_attention'], diary['incorrect_attention']],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
               
            ],
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio:false,
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});


var percepcion = document.getElementById('percepcion').getContext('2d');

var percepcion = new Chart(percepcion, {
    type: 'doughnut',
    data: {
        labels: ['Correctas', 'Incorrectas'],
        datasets: [{
            label: '# of Votes',
            data: [diary['correct_perception'], diary['incorrect_perception']],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
               
            ],
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio:false,
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});



var calculo = document.getElementById('calculo').getContext('2d');

var calculo = new Chart(calculo, {
    type: 'doughnut',
    data: {
        labels: ['Correctas', 'Incorrectas'],
        datasets: [{
            label: '# of Votes',
            data: [diary['correct_calculus'], diary['incorrect_calculus']],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
               
            ],
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio:false,
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});

var lenguaje = document.getElementById('lenguaje').getContext('2d');

var lenguaje = new Chart(lenguaje, {
    type: 'doughnut',
    data: {
        labels: ['Correctas', 'Incorrectas'],
        datasets: [{
            label: '# of Votes',
            data: [diary['correct_language'], diary['incorrect_language']],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
               
            ],
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio:false,
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});



if(diary['test_isaac'] != -1){



var test_isaac = document.getElementById('test_isaac').getContext('2d');

var test_isaac = new Chart(test_isaac, {
    type: 'bar',
    data: {
        labels: ['Puntos totales'],
        datasets: [{
            label: 'Puntos obtenidos'  ,
            data: [diary['test_isaac']],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
               
                
            ],
            borderColor: [
                'rgba(255, 99, 132, 0.2)',
           
            ],
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio:false,
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});

    
}else{

    document.getElementById("isaac").style.display = "none"

}

if(diary['test_hodkinson'] != -1){



    var test_hodkinson = document.getElementById('test_hodkinson').getContext('2d');
    
    var test_hodkinson = new Chart(test_hodkinson, {
        type: 'bar',
        data: {
            labels: ['Puntos totales'],
            datasets: [{
                label: 'Puntos obtenidos'  ,
                data: [diary['test_hodkinson']],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                   
                    
                ],
                borderColor: [
                    'rgba(255, 99, 132, 0.2)',
               
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio:false,
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
    
        
    }else{
        document.getElementById("hodkinson").style.display = "none"
    }