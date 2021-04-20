% prepara el repositorio para su despliegue. 
release: sh -c 'python manage.py migrate'
% especifica el comando para lanzar Cognitya
web: sh -c 'gunicorn cognitya.wsgi --log-file -'
