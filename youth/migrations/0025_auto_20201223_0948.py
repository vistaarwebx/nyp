# Generated by Django 3.1.4 on 2020-12-23 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youth', '0024_auto_20201223_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medias',
            name='video_Link',
            field=models.URLField(null=True),
        ),
    ]
