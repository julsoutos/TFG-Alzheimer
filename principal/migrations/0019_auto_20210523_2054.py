# Generated by Django 3.1.2 on 2021-05-23 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0018_auto_20210523_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='category',
            field=models.CharField(choices=[('None', 'None'), ('Memoria', 'Memory'), ('Atencion', 'Attention'), ('Calculo', 'Calculus'), ('Percepcion', 'Perception'), ('Lenguaje', 'Language')], default='None', max_length=10),
        ),
    ]