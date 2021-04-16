% prepara el repositorio para su despliegue. 
release: sh -c 'python manage.py migrate'
% especifica el comando para lanzar Decide
web: sh -c 'gunicorn decide.wsgi --log-file -'
