# Generated by Django 3.1.4 on 2020-12-28 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youth', '0053_volunteers_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobinternship',
            name='image',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='jobinternship',
            name='resume',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
