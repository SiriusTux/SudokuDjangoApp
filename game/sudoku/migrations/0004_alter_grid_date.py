# Generated by Django 4.1.3 on 2022-12-29 18:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sudoku', '0003_alter_grid_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grid',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 12, 29, 18, 35, 29, 171585, tzinfo=datetime.timezone.utc)),
        ),
    ]