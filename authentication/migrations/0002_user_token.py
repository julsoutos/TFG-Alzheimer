# Generated by Django 3.1.2 on 2021-04-26 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
