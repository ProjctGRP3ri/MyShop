# Generated by Django 3.2.9 on 2022-01-12 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0009_auto_20220112_1150'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='livingroom',
            options={'ordering': ['-ProductID']},
        ),
    ]