% prepara el repositorio para su despliegue. 
release: sh -c 'python manage.py makemigrations principal'
release: sh -c 'python manage.py migrate principal'
% especifica el comando para lanzar Cognitya
web: sh -c 'gunicorn cognitya.wsgi --log-file -'
