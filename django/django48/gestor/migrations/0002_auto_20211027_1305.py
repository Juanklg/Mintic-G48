# Generated by Django 3.2.8 on 2021-10-27 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tareas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proyecto', models.CharField(max_length=15)),
                ('titulo', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=100)),
                ('estado', models.IntegerField(default=0)),
                ('responsable', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='articulos',
            name='nombre',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]
