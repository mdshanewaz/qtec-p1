# Generated by Django 5.0 on 2024-01-08 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductApp', '0002_alter_brandmodel_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warrantymodel',
            name='year',
            field=models.PositiveIntegerField(max_length=10),
        ),
    ]