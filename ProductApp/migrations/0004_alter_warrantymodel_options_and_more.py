# Generated by Django 5.0 on 2024-01-10 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProductApp', '0003_alter_warrantymodel_year'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='warrantymodel',
            options={'ordering': ['year'], 'verbose_name_plural': 'Warranties'},
        ),
        migrations.RenameField(
            model_name='productmodle',
            old_name='brand',
            new_name='brandbrand',
        ),
    ]