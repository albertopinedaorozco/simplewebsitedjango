# Generated by Django 2.1 on 2019-01-14 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('descripcion', models.TextField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='media/')),
                ('nombre', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academico.Asignatura')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academico.Docente')),
            ],
        ),
    ]
