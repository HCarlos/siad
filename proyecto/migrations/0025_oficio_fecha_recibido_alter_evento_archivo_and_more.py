# Generated by Django 4.0 on 2022-03-04 19:50

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0024_alter_evento_archivo_alter_oficio_archivo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='oficio',
            name='fecha_recibido',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='eventos/2022/3/4/'),
        ),
        migrations.AlterField(
            model_name='oficio',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='oficios/2022/3/4/'),
        ),
        migrations.AlterField(
            model_name='oficio',
            name='fecha_respuesta',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 3, 7, 13, 50, 10, 256248), null=True),
        ),
    ]