# Generated by Django 4.1 on 2022-09-02 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0002_bebidas_galletitas_lacteos_delete_hermana_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bebidas',
            old_name='sabor',
            new_name='tipo',
        ),
        migrations.RenameField(
            model_name='galletitas',
            old_name='sabor',
            new_name='tipo',
        ),
    ]
