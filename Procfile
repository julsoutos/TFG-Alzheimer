% prepara el repositorio para su despliegue. 
release: sh -c 'python manage.py makemigrations principal && python manage.py migrate principal && sudo -u postgres psql cognitya < 'datos.sql''
% especifica el comando para lanzar Cognitya
web: sh -c 'gunicorn cognitya.wsgi --log-file -'
