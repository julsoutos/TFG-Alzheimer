INSERT INTO public.principal_user ("password",last_login,is_superuser,username,email,is_staff,is_active,date_joined,is_medic,is_patient,first_name,last_name,birth_date,"comments",save_session) VALUES
	 ('pbkdf2_sha256$216000$f6uYG560Aq18$rqjnhoF0PN1L+0R9o9jnJAPXlu9YluRlnhrYFA4vo08=',NULL,false,'patient','pabrodgar9@alum.us.es',false,true,'2021-06-04 00:03:42.198161+02',false,true,'patient','patient','1946-01-10','',false),
	 ('pbkdf2_sha256$216000$KdIQLfQ4cdMV$ltxC1h41qR6ZOUbkOuVyPURzouehXroOSnivyqY1DiM=','2021-06-04 00:00:29.710118+02',true,'admin','peligron12@gmail.com',true,true,'2021-06-02 18:29:38+02',false,false,'Pablito','Rodriguez','2019-08-06','',false),
	 ('pbkdf2_sha256$216000$ZiNzI2hBQTqZ$7eh4N8FVQ2viT8nUGhrC+boyf4chVnvc6wbBSdNDeDU=',NULL,false,'doctor','prodriguezgarrido11@gmail.com',false,true,'2021-06-04 00:02:36.269423+02',true,false,'doctor','doctor','1999-01-14','',false);

INSERT INTO public.principal_patient (user_id,sickness,doctor_id,address,city) VALUES
	 (30,'Alzheimer',29,'C/Lope de Vega','Dos Hermanas');

INSERT INTO public.principal_doctor (user_id,specialty) VALUES
	 (29,'Neurología');

INSERT INTO public.principal_activity ("name",category,title,description) VALUES
	 ('Calculate Price','Calculus','Calcular precio','Activity'),
	 ('Letter Soup','Attention','Encuentra la palabra','Activity'),
	 ('Locate a letter','Attention','Localiza la letra indicada','Activity'),
	 ('Color Order','Memory','Recuerda la secuencia de colores','Activity'),
	 ('Image Order','Memory','Recuerda el orden de las imágenes','Activity'),
	 ('Sentence Order','Language','Ordenar Frases','Activity'),
	 ('Word Category','Language','Clasificar palabra','Activity'),
	 ('Reorder Image','Perception','Reconstruir Imagen','Activity'),
	 ('Similar Image','Perception','Imagen Similar','Activity'),
	 ('Math Operations','Calculus','Sumas y restas','Activity');

INSERT INTO public.principal_solution (solution,activity_id,"name") VALUES
	 ('1',3,'Image Order 2'),
	 ('1',3,'Image Order 3'),
	 ('3',3,'Image Order 1'),
	 ('e',5,'Locate a letter 1'),
	 ('o',5,'Locate a letter 2'),
	 ('z',5,'Locate a letter 3'),
	 ('n',5,'Locate a letter 4'),
	 ('c',5,'Locate a letter 5'),
	 ('otoño',6,'Letter Soup 1'),
	 ('nata',6,'Letter Soup 2');
INSERT INTO public.principal_solution (solution,activity_id,"name") VALUES
	 ('kiosco',6,'Letter Soup 3'),
	 ('agua',6,'Letter Soup 4'),
	 ('coche',6,'Letter Soup 5'),
	 ('perro',6,'Letter Soup 6'),
	 ('lata',6,'Letter Soup 7'),
	 ('papel',6,'Letter Soup 8'),
	 ('12.20',7,'Calculate Price 1'),
	 ('32.10',7,'Calculate Price 2'),
	 ('20.50',7,'Calculate Price 3'),
	 ('Juan tiene dos hermanos cocineros',8,'Sentence Order 2');
INSERT INTO public.principal_solution (solution,activity_id,"name") VALUES
	 ('¿A qué hora llegas mañana?',8,'Sentence Order 3'),
	 ('El coche blanco tiene 5 ruedas',8,'Sentence Order 1'),
	 ('palanca',9,'Word Category 1'),
	 ('mentón',9,'Word Category 2'),
	 ('comercial',9,'Word Category 3'),
	 ('metro',9,'Word Category 4'),
	 ('1',11,'Similar Image'),
	 ('123456',10,'Reorder Image'),
	 ('1663',4,'Color Order 1'),
	 ('3115',4,'Color Order 2');
INSERT INTO public.principal_solution (solution,activity_id,"name") VALUES
	 ('2451',4,'Color Order 3'),
	 ('17',12,'Math Operations 1'),
	 ('51',12,'Math Operations 2'),
	 ('19',12,'Math Operations 3');

INSERT INTO public.principal_mental_test ("name",description,title) VALUES
	 ('Hodkinson Test','Mental Test','Test de Hodkinson Abreviado'),
	 ('Isaac Test','Mental Test','Test de Isaac');

