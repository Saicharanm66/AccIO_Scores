# Generated by Django 4.0.4 on 2022-06-09 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_alter_scoreupdate_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scoreupdate',
            name='over',
            field=models.FloatField(),
        ),
    ]
