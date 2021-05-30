function setDay(value){

    document.getElementById("sendDay").click()

}






if(document.getElementById("day").value != ""){


    

var comparativaSemanal = document.getElementById('comparativaSemanal').getContext('2d');
var comparativaSemanal = new Chart(comparativaSemanal, {
    type: 'bar',
    data: {
        labels: ['Día 1', 'Día 2', 'Día 3', 'Día 4', 'Día 5', 'Día 6' ,'Día 7'],
        datasets: [{
            label: ['Correctas'],
            data: [ week["week_days"][0][0], week["week_days"][1][0], week["week_days"][2][0], week["week_days"][3][0], week["week_days"][4][0], week["week_days"][5][0], week["week_days"][6][0] ],
            backgroundColor: [
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',

            ],
            borderColor: [
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',

               
            ],
            borderWidth: 1
        },{
            label: ['Incorrectas'],
            data: [ week["week_days"][0][1], week["week_days"][1][1], week["week_days"][2][1], week["week_days"][3][1], week["week_days"][4][1], week["week_days"][5][1], week["week_days"][6][1] ],
            backgroundColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',

            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',

            ],
            borderWidth: 1
        }

        
    ]
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



var comparativaSemana2 = document.getElementById('comparativaSemana2').getContext('2d');
var comparativaSemana2 = new Chart(comparativaSemana2, {
    type: 'radar',
    data: {
        labels: ['MEMORIA','ATENCION','PERCEPCION','CALCULO','LENGUAJE'],
        datasets: [{
            label: ['Correctas'],
            data: [week["correct_memory"], week["correct_attention"], week["correct_perception"], week["correct_calculus"], week["correct_language"]],
            backgroundColor: [
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                
            ],
            borderColor: [
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                

               
            ],
            borderWidth: 1
        },{
            label: ['Incorrectas'],
            data: [week["incorrect_memory"], week["incorrect_attention"], week["incorrect_perception"], week["incorrect_calculus"], week["incorrect_language"]],
            backgroundColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                

            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
              

            ],
            borderWidth: 1 
        }

        
    ]
    },
    options: {
        responsive: true,
        maintainAspectRatio:false,
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true,
                    
                }
            }]
        } 
        
    }
});


//Gráfica tests


// var testSemanal = document.getElementById('testSemanal').getContext('2d');

// var testSemanal = new Chart(testSemanal, {
//     type: 'line',
//     data: {
//         labels: ['Día 1', 'Día 2', 'Día 3', 'Día 4', 'Día 5', 'Día 6' ,'Día 7'],
//         datasets: [{
//             label: 'Puntos por día',
//             data: [8,5,7,6,8,6,7],
//             backgroundColor: [
//                 'rgba(255, 99, 132, 0.2)',
//                 'rgba(54, 162, 235, 0.2)',
//                 'rgba(255, 206, 86, 0.2)',
//                 'rgba(75, 192, 192, 0.2)',

                
//             ],
//             borderColor: [
//                 'rgba(255, 99, 132, 0.2)',
//                 'rgba(54, 162, 235, 0.2)',
//                 'rgba(255, 206, 86, 0.2)',
//                 'rgba(75, 192, 192, 0.2)',
               
//             ],
//             borderWidth: 1
//         }]
//     },
//     options: {
//         responsive: true,
//         maintainAspectRatio:false,
//         scales: {
//             yAxes: [{
//                 ticks: {
//                     beginAtZero: true
//                 }
//             }]
//         }
//     }
// });








var comparativaMensual1 = document.getElementById('comparativaMensual1').getContext('2d');
var comparativaMensual1 = new Chart(comparativaMensual1, {
    type: 'bar',
    data: {
        labels: ['Semana 1', 'Semana 2', 'Semana 3', 'Semana 4'],
        datasets: [{
            label: ['Correctas'],
            data: [month["week_days"][0][0],month["week_days"][1][0],month["week_days"][2][0],month["week_days"][3][0]],
            backgroundColor: [
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
               

            ],
            borderColor: [
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
               

               
            ],
            borderWidth: 1
        },{
            label: ['Incorrectas'],
            data: [month["week_days"][0][1], month["week_days"][1][1], month["week_days"][2][1], month["week_days"][3][1]],
            backgroundColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
               

            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
              

            ],
            borderWidth: 1
        }

        
    ]
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



var comparativaMensual2 = document.getElementById('comparativaMensual2').getContext('2d');
var comparativaMensual2 = new Chart(comparativaMensual2, {
    type: 'radar',
    data: {
        labels: ['MEMORIA','ATENCION','PERCEPCION','CALCULO','LENGUAJE'],
        datasets: [{
            label: ['Correctas'],
            data: [month["correct_memory"],month["correct_attention"],month["correct_perception"],month["correct_calculus"],month["correct_language"]],
            backgroundColor: [
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                
            ],
            borderColor: [
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                

               
            ],
            borderWidth: 1
        },{
            label: ['Incorrectas'],
            data: [month["incorrect_memory"],month["incorrect_attention"],month["incorrect_perception"],month["incorrect_calculus"],month["incorrect_language"]],
            backgroundColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                

            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
              

            ],
            borderWidth: 1 
        }

        
    ]
    },
    options: {
        responsive: true,
        maintainAspectRatio:false,
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true,
                    
                }
            }]
        } 
        
    }
});





// var testMensual = document.getElementById('testMensual').getContext('2d');

// var testMensual = new Chart(testMensual, {
//     type: 'line',
//     data: {
//         labels: ['Semana 1', 'Semana 2', 'Semana 3', 'Semana 4'],
//         datasets: [{
//             label: 'Puntos por semana',
//             data: [10,11,12,13],
//             backgroundColor: [
//                 'rgba(255, 99, 132, 0.2)',
//                 'rgba(54, 162, 235, 0.2)',
//                 'rgba(255, 206, 86, 0.2)',
//                 'rgba(75, 192, 192, 0.2)',

                
//             ],
//             borderColor: [
//                 'rgba(255, 99, 132, 0.2)',
//                 'rgba(54, 162, 235, 0.2)',
//                 'rgba(255, 206, 86, 0.2)',
//                 'rgba(75, 192, 192, 0.2)',
               
//             ],
//             borderWidth: 1
//         }]
//     },
//     options: {
//         responsive: true,
//         maintainAspectRatio:false,
//         scales: {
//             yAxes: [{
//                 ticks: {
//                     beginAtZero: true
//                 }
//             }]
//         }
//     }
// });











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


// var test = document.getElementById('test').getContext('2d');

// var test = new Chart(test, {
//     type: 'line',
//     data: {
//         labels: ['Pregunta 1', 'Pregunta 2', 'Pregunta 3', 'Pregunta 4'],
//         datasets: [{
//             label: 'Puntos por pregunta',
//             data: [1, 3, 2, 2],
//             backgroundColor: [
//                 'rgba(255, 99, 132, 0.2)',
//                 'rgba(54, 162, 235, 0.2)',
//                 'rgba(255, 206, 86, 0.2)',
//                 'rgba(75, 192, 192, 0.2)',

                
//             ],
//             borderColor: [
//                 'rgba(255, 99, 132, 0.2)',
//                 'rgba(54, 162, 235, 0.2)',
//                 'rgba(255, 206, 86, 0.2)',
//                 'rgba(75, 192, 192, 0.2)',
               
//             ],
//             borderWidth: 1
//         }]
//     },
//     options: {
//         responsive: true,
//         maintainAspectRatio:false,
//         scales: {
//             yAxes: [{
//                 ticks: {
//                     beginAtZero: true
//                 }
//             }]
//         }
//     }
// });

}
