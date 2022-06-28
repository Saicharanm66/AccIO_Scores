# Generated by Django 4.0.4 on 2022-06-05 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_rename_teammembers_teammember_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='scoreupdate',
            name='Player_type',
            field=models.CharField(choices=[('6', '6'), ('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1'), ('0', '0')], default='6', max_length=20),
        ),
        migrations.AddField(
            model_name='scoreupdate',
            name='currentbat1',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scoreupdate',
            name='currentbat2',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scoreupdate',
            name='currentbowler',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scoreupdate',
            name='overs',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scoreupdate',
            name='wickets',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teammember',
            name='Player_side',
            field=models.CharField(choices=[('Right hand', 'Right hand'), ('Left hand', 'Left hand')], default='Right hand', max_length=20),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='player_img',
            field=models.ImageField(upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='player_name',
            field=models.CharField(max_length=100),
        ),
    ]