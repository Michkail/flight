# Generated by Django 3.1 on 2020-08-24 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightnumber', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightnumber',
            name='category',
            field=models.CharField(choices=[('C', 'Code'), ('B', 'Boeing')], max_length=12),
        ),
    ]
