# Generated by Django 2.1 on 2019-01-14 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0002_auto_20190114_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
