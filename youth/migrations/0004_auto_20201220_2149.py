# Generated by Django 3.1.4 on 2020-12-21 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youth', '0003_hello'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='memAddress',
        ),
        migrations.RemoveField(
            model_name='member',
            name='memCity',
        ),
        migrations.AddField(
            model_name='member',
            name='memeducation',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='memoccupation',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='memposition',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
