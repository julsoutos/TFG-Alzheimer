
var memoria = document.getElementById('memoria').getContext('2d');

var memoria = new Chart(memoria, {
    type: 'doughnut',
    data: {
        labels: ['Correctas', 'Incorrectas'],
        datasets: [{
            label: '# of Votes',
            data: [2, 3],
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
            data: [1, 2],
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
            data: [1, 1],
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
            data: [1, 0],
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
            data: [0, 0],
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
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});


var test = document.getElementById('test').getContext('2d');

var test = new Chart(test, {
    type: 'line',
    data: {
        labels: ['Pregunta 1', 'Pregunta 2', 'Pregunta 3', 'Pregunta 4'],
        datasets: [{
            label: 'Puntos obtenidos por pregunta',
            data: [1, 3, 2, 2],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',

                
            ],
            borderColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
               
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});