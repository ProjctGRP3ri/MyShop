# Generated by Django 3.2.9 on 2022-01-10 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0004_auto_20220110_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studyroom',
            name='IMG',
            field=models.CharField(max_length=2500),
        ),
        migrations.AlterField(
            model_name='studyroom',
            name='Title',
            field=models.CharField(max_length=500),
        ),
    ]