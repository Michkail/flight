# Generated by Django 3.1 on 2020-08-23 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArrivalPort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('category', models.CharField(choices=[('LAT', 'Latitude'), ('LNG', 'Longtitude')], max_length=200)),
            ],
            options={
                'verbose_name': 'ArrivalPort',
                'verbose_name_plural': 'ArrivalPort',
            },
        ),
    ]
