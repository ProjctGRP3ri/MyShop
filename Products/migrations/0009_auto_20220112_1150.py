# Generated by Django 3.2.9 on 2022-01-12 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0008_auto_20220112_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livingroom',
            name='IMGSet1',
            field=models.CharField(max_length=2500, null=True),
        ),
        migrations.AlterField(
            model_name='livingroom',
            name='IMGSet2',
            field=models.CharField(max_length=2500, null=True),
        ),
        migrations.AlterField(
            model_name='livingroom',
            name='IMGSet3',
            field=models.CharField(max_length=2500, null=True),
        ),
        migrations.AlterField(
            model_name='livingroom',
            name='IMGSet4',
            field=models.CharField(max_length=2500, null=True),
        ),
    ]
