# Generated by Django 3.1.4 on 2020-12-22 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youth', '0007_auto_20201221_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facebook',
            name='image',
            field=models.FileField(max_length=6, null=True, upload_to=''),
        ),
    ]
