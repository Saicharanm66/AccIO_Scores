# Generated by Django 4.0.4 on 2022-06-04 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='Status',
            field=models.CharField(choices=[('Ongoing', 'ongoing'), ('Scheduled', 'Scheduled'), ('Cancelled', 'Cancelled')], default='Scheduled', max_length=9),
        ),
    ]
