# Generated by Django 3.2.9 on 2022-01-17 06:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Users', '0009_alter_registernewuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registernewuser',
            name='username',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
