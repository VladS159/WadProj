# Generated by Django 3.2.9 on 2022-10-23 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_followerscount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followerscount',
            name='follower',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='followerscount',
            name='user',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='likepost',
            name='username',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.CharField(max_length=500),
        ),
    ]