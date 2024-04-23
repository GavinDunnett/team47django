# Generated by Django 5.0.2 on 2024-04-17 02:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airline_app', '0019_airport_dst'),
    ]

    operations = [
        migrations.AddField(
            model_name='airline',
            name='customer_rating',
            field=models.DecimalField(decimal_places=3, default=0.75, max_digits=4),
        ),
        migrations.AlterField(
            model_name='airport',
            name='arrival_delay',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='airport',
            name='departure_delay',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='fleet',
            name='next_a_check',
            field=models.DateField(default=datetime.date(2024, 6, 26)),
        ),
        migrations.AlterField(
            model_name='fleet',
            name='next_b_check',
            field=models.DateField(default=datetime.date(2025, 1, 22)),
        ),
        migrations.AlterField(
            model_name='fleet',
            name='next_c_check',
            field=models.DateField(default=datetime.date(2025, 10, 29)),
        ),
        migrations.AlterField(
            model_name='fleet',
            name='next_d_check',
            field=models.DateField(default=datetime.date(2031, 12, 17)),
        ),
    ]