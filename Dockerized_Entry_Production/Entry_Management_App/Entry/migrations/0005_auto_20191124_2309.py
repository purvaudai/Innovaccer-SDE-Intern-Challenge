# Generated by Django 2.2.7 on 2019-11-24 23:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Entry', '0004_auto_20191124_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='hostuser', to=settings.AUTH_USER_MODEL),
        ),
    ]
