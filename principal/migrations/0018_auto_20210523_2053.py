# Generated by Django 3.1.2 on 2021-05-23 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0017_auto_20210523_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='category',
            field=models.CharField(choices=[('None', 'None'), ('Memoria', 'Memory'), ('Atencion', 'Atención'), ('Calculo', 'Cálculo'), ('Percepcion', 'Percepción'), ('Lenguaje', 'Lenguaje')], default='None', max_length=10),
        ),
    ]
