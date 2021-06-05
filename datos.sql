INSERT INTO public.principal_user ("password",last_login,is_superuser,username,email,is_staff,is_active,date_joined,is_medic,is_patient,first_name,last_name,birth_date,"comments",save_session) VALUES
	 ('pbkdf2_sha256$216000$ZiNzI2hBQTqZ$7eh4N8FVQ2viT8nUGhrC+boyf4chVnvc6wbBSdNDeDU=','2021-06-05 11:03:27.802146+02',false,'doctor','doctor@gmail.com',false,true,'2021-06-04 00:02:36.269423+02',true,false,'doctor','doctor','1999-01-14','',false),
	 ('pbkdf2_sha256$216000$f6uYG560Aq18$rqjnhoF0PN1L+0R9o9jnJAPXlu9YluRlnhrYFA4vo08=','2021-06-05 11:05:04.77753+02',false,'patient','patient@alum.us.es',false,true,'2021-06-04 00:03:42+02',false,true,'patient','patient','1946-01-10','Estado de no demencia',false),
	 ('pbkdf2_sha256$216000$5gpFAhB414jN$/4ikZ0w+2p3+pCyGcd81cBH4kkamccYhdrXiM7q4p0Q=','2021-06-05 11:28:17.98581+02',true,'admin','admin@gmail.com',true,true,'2021-06-02 18:29:38+02',false,false,'Pablo','Rodriguez','1999-08-06','',false);

INSERT INTO public.principal_doctor (user_id,specialty) VALUES
	 (1,'Neurología');

INSERT INTO public.principal_patient (user_id,sickness,doctor_id,address,city) VALUES
	 (2,'Alzheimer',1,'C/Lope de Vega','Dos Hermanas');

INSERT INTO public.principal_activity (name,category,title,description) VALUES
	 ('Math Operations','Calculus','Sumas y restas','En esta actividad el paciente deberá de realizar diferentes operaciones simples de suma y resta.'),
	 ('Similar Image','Perception','Imagen Similar','En esta actividad el paciente deberá de percibir qué imagen es similar a la generada por el sistema. Las imágenes estarán compuestas por diferentes figuras geométricas a las que se les ha aplicado pequeñas diferencias entre sí.'),
	 ('Reorder Image','Perception','Reconstruir Imagen','En esta actividad el paciente deberá de recomponer una imagen que ha sido dividida en 6 fragmentos y repartidos por la pantalla de forma aleatoria.'),
	 ('Word Category','Language','Clasificar palabra','En esta actividad el paciente deberá de elegir la palabra que se identifique con el enunciado generado.'),
	 ('Sentence Order','Language','Ordenar Frases','En esta actividad el paciente deberá de formar una oración a partir de una serie de palabras dadas.'),
	 ('Calculate Price','Calculus','Calcular precio','En esta actividad el paciente deberá de obtener un precio a partir de las diferentes "monedas" proporcionadas.'),
	 ('Letter Soup','Attention','Encuentra la palabra','En esta actividad el paciente deberá de resolver una pequeña sopa de letras dónde deberá de encontrar un palabra dada.'),
	 ('Locate a letter','Attention','Localiza la letra indicada','En esta actividad el paciente deberá de encontrar la letra que se haya indicado entre conjunto aleatorio dado.'),
	 ('Color Order','Memory','Recuerda la secuencia de colores','En esta actividad el paciente deberá de memorizar y replicar una secuencia de 4 patrones de colores.'),
	 ('Image Order','Memory','Recuerda el orden de las imágenes','En esta actividad el paciente deberá de indicar cuál es el orden correcto indicado al inicio de una serie de 3 imágenes.');

INSERT INTO public.principal_solution (solution,activity_id,name) VALUES
	 ('1',10,'Image Order 2'),
	 ('1',10,'Image Order 3'),
	 ('3',10,'Image Order 1'),
	 ('e',8,'Locate a letter 1'),
	 ('o',8,'Locate a letter 2'),
	 ('z',8,'Locate a letter 3'),
	 ('n',8,'Locate a letter 4'),
	 ('c',8,'Locate a letter 5'),
	 ('otoño',7,'Letter Soup 1'),
	 ('nata',7,'Letter Soup 2');
INSERT INTO public.principal_solution (solution,activity_id,name) VALUES
	 ('kiosco',7,'Letter Soup 3'),
	 ('agua',7,'Letter Soup 4'),
	 ('coche',7,'Letter Soup 5'),
	 ('perro',7,'Letter Soup 6'),
	 ('lata',7,'Letter Soup 7'),
	 ('papel',7,'Letter Soup 8'),
	 ('12.20',6,'Calculate Price 1'),
	 ('32.10',6,'Calculate Price 2'),
	 ('20.50',6,'Calculate Price 3'),
	 ('Está lloviendo mucho en la calle',5,'Sentence Order 2');
INSERT INTO public.principal_solution (solution,activity_id,name) VALUES
	 ('¿A qué hora llegas mañana?',5,'Sentence Order 3'),
	 ('Ese perro es muy bonito',5,'Sentence Order 1'),
	 ('palanca',4,'Word Category 1'),
	 ('mentón',4,'Word Category 2'),
	 ('comercial',4,'Word Category 3'),
	 ('metro',4,'Word Category 4'),
	 ('1',2,'Similar Image'),
	 ('123456',3,'Reorder Image'),
	 ('1663',9,'Color Order 1'),
	 ('3115',9,'Color Order 2');
INSERT INTO public.principal_solution (solution,activity_id,name) VALUES
	 ('2451',9,'Color Order 3'),
	 ('17',1,'Math Operations 1'),
	 ('51',1,'Math Operations 2'),
	 ('19',1,'Math Operations 3');


INSERT INTO public.principal_mental_test (name,description,title) VALUES
	 ('Hodkinson Test','En este test el paciente deberá responder a una serie de preguntas, recibiendo un punto por cada correcta. Si obtiene entre 1 y 2 puntos será deterioro severo, entre 4 y 5 deterioro moderado y entre 5 y 6 deterioro leve. Si consigue 7 puntos, se considerará que no hay deterioro.','Test de Hodkinson Abreviado'),
	 ('Isaac Test','En este test el paciente deberá seleccionar una serie de palabras pertenecientes a diferentes categorías: animales, frutas y colores. El número ideal de palabras seleccionadas en un adulto serían 29 o más aciertos, y de 27  o más si se trata de ancianos.','Test de Isaac');