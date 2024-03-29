# Generated by Django 4.0 on 2022-06-22 18:48

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import siad.functions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0009_alter_usuario_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dependencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dependencia', models.CharField(max_length=250)),
                ('abreviatura', models.CharField(max_length=25)),
                ('modi_el', models.DateField(blank=True, null=True, verbose_name='died')),
                ('modi_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dep_modi_por', to='home.usuario')),
                ('titular', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dep_titular', to='home.usuario')),
            ],
            options={
                'verbose_name': 'Dependencia',
                'verbose_name_plural': 'Dependencias',
                'ordering': ['dependencia'],
            },
        ),
        migrations.CreateModel(
            name='UnidadMedida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidad', models.CharField(max_length=250)),
                ('abreviatura', models.CharField(max_length=25)),
                ('modi_el', models.DateField(blank=True, null=True, verbose_name='died')),
                ('modi_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='medida_modi_por', to='home.usuario')),
            ],
            options={
                'verbose_name': 'Unidad de Medida',
                'verbose_name_plural': 'Unidades de medida',
                'ordering': ['unidad'],
            },
        ),
        migrations.CreateModel(
            name='Subdireccione',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subdireccion', models.CharField(max_length=250)),
                ('abreviatura', models.CharField(max_length=25)),
                ('cargo', models.CharField(max_length=250)),
                ('is_visible', models.BooleanField(default=False)),
                ('modi_el', models.DateField(blank=True, null=True, verbose_name='died')),
                ('dependencia', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subdir_dependencia', to='proyecto.dependencia')),
                ('modi_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subdir_modi_por', to='home.usuario')),
                ('titular', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titular_subdirector', to='home.usuario')),
            ],
            options={
                'verbose_name': 'Subdirección',
                'verbose_name_plural': 'Subdirecciones',
                'ordering': ['subdireccion'],
            },
        ),
        migrations.CreateModel(
            name='Respuestas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta', models.CharField(default='', max_length=2000)),
                ('fecha_respuesta', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('estatus', models.SmallIntegerField(choices=[(0, 'RECIBIDO'), (1, 'EN PROCESO'), (2, 'TURNADO A OTRA DEPENDENCIA'), (3, 'NO PROCEDE'), (4, 'RESUELTO FAVORABLE'), (5, 'RESUELTO NO FAVORABLE')], default=0)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='oficios_respuestas/2022/6/22/', validators=[siad.functions.validate_file_extension, siad.functions.file_size])),
                ('archivo_datetime', models.DateTimeField(auto_now=True, null=True)),
                ('creado_el', models.DateField(blank=True, null=True, verbose_name='died')),
                ('modi_el', models.DateField(blank=True, null=True, verbose_name='died')),
                ('creado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='respuesta_creado_por', to='home.usuario')),
                ('modi_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='respuesta_modi_por', to='home.usuario')),
            ],
            options={
                'verbose_name': 'Respuesta',
                'verbose_name_plural': 'Respuestas',
                'ordering': ['-pk'],
                'permissions': (('Puede Crear', 'Puede Editar'),),
            },
        ),
        migrations.CreateModel(
            name='Oficio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anno', models.IntegerField(blank=True, default=2022, null=True)),
                ('tipo_documento', models.SmallIntegerField(blank=True, choices=[(0, 'RECIBIDOS'), (1, 'FIRMADOS POR EL(LA) DIRECTOR(A)')], default=1, null=True)),
                ('consecutivo', models.IntegerField(blank=True, default=0, null=True)),
                ('oficio', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('fecha_documento', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('remitente', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('del_remitente', models.CharField(default='', max_length=250)),
                ('asunto', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('instrucciones', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('fecha_captura', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('fecha_recibido', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('fecha_respuesta', models.DateField(blank=True, default=datetime.datetime(2022, 6, 25, 13, 48, 55, 734934), null=True)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='oficios/2022/6/22/', validators=[siad.functions.validate_file_extension, siad.functions.file_size])),
                ('archivo_datetime', models.DateTimeField(auto_now=True, null=True)),
                ('creado_el', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('modi_el', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('creado_por', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ofi_creado_por', to='home.usuario')),
                ('dir_remitente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='oficio_dir_remitente_dep', to='proyecto.dependencia')),
                ('modi_por', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ofi_modi_por', to='home.usuario')),
                ('recibe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='oficio_recibe_dep', to='proyecto.subdireccione')),
                ('respuestas', models.ManyToManyField(to='proyecto.Respuestas')),
                ('subdireccion', models.ManyToManyField(to='proyecto.Subdireccione')),
            ],
            options={
                'verbose_name': 'Oficio',
                'verbose_name_plural': 'Oficios',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anno', models.IntegerField(blank=True, default=2022, null=True)),
                ('fecha_evento', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('hora_evento', models.TimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('asunto', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('lugar', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('seguimiento', models.TextField(blank=True, default='', max_length=4000, null=True)),
                ('respuesta', models.TextField(blank=True, default='', max_length=4000, null=True)),
                ('fecha_respuesta', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='eventos/2022/6/22/')),
                ('archivo_datetime', models.DateTimeField(auto_now=True, null=True)),
                ('creado_el', models.DateField(blank=True, null=True, verbose_name='died')),
                ('modi_el', models.DateField(blank=True, null=True, verbose_name='died')),
                ('creado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='evento_creado_por', to='home.usuario')),
                ('dependencia_solicita', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='evento_solicita_dep', to='proyecto.dependencia')),
                ('modi_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='evento_modi_por', to='home.usuario')),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
                'ordering': ['pk'],
                'permissions': (('Puede Crear', 'Puede Editar'),),
            },
        ),
    ]
