# Generated by Django 4.0.1 on 2022-01-31 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mfgadmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotions',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='promotions',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='promotions',
            name='start_date',
            field=models.DateField(),
        ),
    ]