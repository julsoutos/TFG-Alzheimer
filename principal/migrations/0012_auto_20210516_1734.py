# Generated by Django 3.1.2 on 2021-05-16 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0011_auto_20210516_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity_training',
            name='training',
        ),
        migrations.AddField(
            model_name='activity_training',
            name='patient_training',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='principal.patient_training'),
        ),
    ]
