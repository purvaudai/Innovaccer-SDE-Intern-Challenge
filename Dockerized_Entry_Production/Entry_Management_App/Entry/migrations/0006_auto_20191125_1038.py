# Generated by Django 2.2.7 on 2019-11-25 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Entry', '0005_auto_20191124_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
