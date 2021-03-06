# Generated by Django 3.2.9 on 2022-01-21 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0012_remove_registernewuser_main_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyOrders',
            fields=[
                ('OrderId', models.IntegerField(primary_key=True, serialize=False)),
                ('UserName', models.CharField(max_length=255)),
                ('ProductID', models.IntegerField(null=True)),
                ('OrderDate', models.DateTimeField(auto_now_add=True)),
                ('ProductImage', models.CharField(max_length=2500)),
                ('ProductCategory', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['-OrderDate'],
            },
        ),
    ]
