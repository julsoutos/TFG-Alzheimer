% prepara el repositorio para su despliegue. 
release: sh -c 'python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic'
% especifica el comando para lanzar Cognitya
web: sh -c 'gunicorn cognitya.wsgi --log-file -'
