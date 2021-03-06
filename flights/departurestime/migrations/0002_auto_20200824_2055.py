# Generated by Django 3.1 on 2020-08-24 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departurestime', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departurestime',
            name='clock',
            field=models.CharField(choices=[('T00', '09:00:23Z'), ('T01', '10:00:23Z'), ('T02', '11:00:23Z'), ('T03', '12:00:23Z'), ('T04', '13:00:23Z'), ('T05', '14:00:23Z'), ('T06', '15:00:23Z'), ('T07', '16:00:23Z'), ('T08', '17:00:23Z'), ('T09', '18:00:23Z'), ('T10', '19:00:23Z'), ('T11', '20:00:23Z')], max_length=50),
        ),
        migrations.AlterField(
            model_name='departurestime',
            name='date',
            field=models.CharField(choices=[('A', '2020-06-10'), ('B', '2020-06-11'), ('C', '2020-06-12'), ('D', '2020-06-13'), ('E', '2020-06-14'), ('F', '2020-06-15'), ('G', '2020-06-16'), ('H', '2020-06-17'), ('I', '2020-06-18'), ('J', '2020-06-19'), ('K', '2020-06-20'), ('L', '2020-06-21'), ('M', '2020-06-22'), ('N', '2020-06-23'), ('O', '2020-06-24'), ('P', '2020-06-25'), ('Q', '2020-06-26'), ('R', '2020-06-26'), ('S', '2020-06-27'), ('T', '2020-06-28')], max_length=50),
        ),
    ]
