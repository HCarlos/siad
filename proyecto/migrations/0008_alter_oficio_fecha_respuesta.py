# Generated by Django 4.0 on 2022-07-08 20:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0007_alter_oficio_fecha_respuesta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oficio',
            name='fecha_respuesta',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 7, 11, 15, 16, 56, 952532), null=True),
        ),
    ]