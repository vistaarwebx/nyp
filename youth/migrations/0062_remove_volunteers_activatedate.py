# Generated by Django 3.1.4 on 2020-12-30 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youth', '0061_group_activatedate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteers',
            name='activatedate',
        ),
    ]
