# Generated by Django 3.1.2 on 2021-05-07 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_auto_20210507_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
