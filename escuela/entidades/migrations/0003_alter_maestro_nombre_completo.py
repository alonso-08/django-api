# Generated by Django 4.1.1 on 2022-10-04 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entidades', '0002_alter_maestro_sueldo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maestro',
            name='nombre_completo',
            field=models.CharField(default='nombre default', max_length=100),
        ),
    ]