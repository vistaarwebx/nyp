# Generated by Django 3.1.4 on 2020-12-22 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youth', '0011_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='posts',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
