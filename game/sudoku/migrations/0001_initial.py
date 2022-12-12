# Generated by Django 4.1.3 on 2022-12-12 18:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grid', models.CharField(max_length=81)),
                ('difficulty', models.CharField(default='easy', max_length=10)),
                ('source', models.CharField(default='Unknown', max_length=255)),
                ('date', models.DateField(default=datetime.datetime(2022, 12, 12, 18, 15, 18, 175744))),
            ],
        ),
    ]
