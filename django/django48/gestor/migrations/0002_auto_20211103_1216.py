# Generated by Django 3.2.8 on 2021-11-03 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientes',
            name='tfno',
        ),
        migrations.AddField(
            model_name='clientes',
            name='password',
            field=models.CharField(default='nulo', max_length=15),
        ),
        migrations.AddField(
            model_name='clientes',
            name='telefono',
            field=models.CharField(default='nulo', max_length=15),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='direccion',
            field=models.CharField(default='nulo', max_length=50),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='email',
            field=models.EmailField(default='nulo', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='nombre',
            field=models.CharField(default='nulo', max_length=30),
        ),
    ]
