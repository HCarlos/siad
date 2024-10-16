# Generated by Django 4.0 on 2023-08-24 18:22

import datetime
from django.db import migrations, models
import siad.functions


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0014_alter_evento_archivo_alter_oficio_archivo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='anno',
            field=models.IntegerField(blank=True, default=2023, null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='eventos/2023/8/24/'),
        ),
        migrations.AlterField(
            model_name='oficio',
            name='anno',
            field=models.IntegerField(blank=True, default=2023, null=True),
        ),
        migrations.AlterField(
            model_name='oficio',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='oficios/2023/8/24/', validators=[siad.functions.validate_file_extension, siad.functions.file_size]),
        ),
        migrations.AlterField(
            model_name='oficio',
            name='fecha_respuesta',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 27, 12, 22, 28, 623275), null=True),
        ),
        migrations.AlterField(
            model_name='respuestas',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='oficios_respuestas/2023/8/24/', validators=[siad.functions.validate_file_extension, siad.functions.file_size]),
        ),
    ]
