# Generated by Django 3.2.9 on 2022-01-13 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0014_auto_20220112_2018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bedroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductID', models.IntegerField(default=True)),
                ('Title', models.CharField(max_length=500)),
                ('AMT', models.FloatField(default=True)),
                ('Discount', models.IntegerField(null=True)),
                ('IMG', models.CharField(max_length=2500)),
                ('IMGSet1', models.CharField(default=True, max_length=2500)),
                ('IMGSet2', models.CharField(default=True, max_length=2500)),
                ('IMGSet3', models.CharField(default=True, max_length=2500)),
                ('IMGSet4', models.CharField(default=True, max_length=2500)),
            ],
            options={
                'ordering': ['ProductID'],
            },
        ),
        migrations.CreateModel(
            name='Kitchenroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductID', models.IntegerField(default=True)),
                ('Title', models.CharField(max_length=500)),
                ('AMT', models.FloatField(default=True)),
                ('Discount', models.IntegerField(null=True)),
                ('IMG', models.CharField(max_length=2500)),
                ('IMGSet1', models.CharField(default=True, max_length=2500)),
                ('IMGSet2', models.CharField(default=True, max_length=2500)),
                ('IMGSet3', models.CharField(default=True, max_length=2500)),
                ('IMGSet4', models.CharField(default=True, max_length=2500)),
            ],
            options={
                'ordering': ['ProductID'],
            },
        ),
    ]
