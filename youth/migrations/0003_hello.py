# Generated by Django 3.1.4 on 2020-12-20 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youth', '0002_auto_20201219_1010'),
    ]

    operations = [
        migrations.CreateModel(
            name='hello',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
            ],
        ),
    ]