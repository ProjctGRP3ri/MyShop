# Generated by Django 3.2.9 on 2022-01-12 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0011_alter_livingroom_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studyroom',
            options={'ordering': ['ProductID']},
        ),
    ]
