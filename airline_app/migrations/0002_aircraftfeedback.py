# Generated by Django 5.0.2 on 2024-03-26 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airline_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AircraftFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200)),
            ],
        ),
    ]
