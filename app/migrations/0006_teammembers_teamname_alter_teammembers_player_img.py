# Generated by Django 4.0.4 on 2022-06-04 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_teammembers_rename_destination_teams'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammembers',
            name='teamname',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teammembers',
            name='player_img',
            field=models.ImageField(upload_to=models.CharField(max_length=100)),
        ),
    ]