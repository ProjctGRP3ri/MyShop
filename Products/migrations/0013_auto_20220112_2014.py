# Generated by Django 3.2.9 on 2022-01-12 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0012_alter_studyroom_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livingroom',
            name='IMGSet1',
            field=models.CharField(default=True, max_length=2500),
        ),
        migrations.AlterField(
            model_name='livingroom',
            name='IMGSet2',
            field=models.CharField(default=True, max_length=2500),
        ),
        migrations.AlterField(
            model_name='livingroom',
            name='IMGSet3',
            field=models.CharField(default=True, max_length=2500),
        ),
        migrations.AlterField(
            model_name='livingroom',
            name='IMGSet4',
            field=models.CharField(default=True, max_length=2500),
        ),
    ]