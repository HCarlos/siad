# Generated by Django 4.0 on 2021-12-28 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_usuario_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='profile/'),
        ),
        migrations.DeleteModel(
            name='Dependencia',
        ),
    ]
