# Generated by Django 3.1.4 on 2020-12-30 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youth', '0062_remove_volunteers_activatedate'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobinternship',
            name='activatedate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='volunteers',
            name='activatedate',
            field=models.DateField(null=True),
        ),
    ]
