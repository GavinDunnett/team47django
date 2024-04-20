# Generated by Django 5.0.2 on 2024-04-20 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airline_app', '0072_alter_flight_is_cancelled'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='is_cancelled',
        ),
        migrations.AddField(
            model_name='flight',
            name='is_canceled',
            field=models.BooleanField(default=False, verbose_name='Canceled'),
        ),
    ]
