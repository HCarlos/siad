# Generated by Django 4.0 on 2022-01-15 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_usuario_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'ordering': ['pk'], 'permissions': (('Crear Usuario', 'Crear Usuario'), ('Editar Usuario', 'Editar Usuario'))},
        ),
    ]
