# Generated by Django 4.2.15 on 2024-08-20 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('task1', '0003_delete_cinema'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('movie_duration', models.CharField(max_length=50)),
                ('movie_year', models.IntegerField(default=1900)),
                ('genres', models.CharField(default=' ', max_length=50)),
                ('countries', models.CharField(default=' ', max_length=40)),
            ],
        ),
    ]
