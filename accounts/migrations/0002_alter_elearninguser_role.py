# Generated by Django 3.2.5 on 2021-07-30 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elearninguser',
            name='role',
            field=models.CharField(choices=[('educator', 'Educator'), ('learner', 'Learner')], max_length=15),
        ),
    ]
