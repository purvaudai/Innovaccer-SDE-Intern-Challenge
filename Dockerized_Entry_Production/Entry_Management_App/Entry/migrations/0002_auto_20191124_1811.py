# Generated by Django 2.2.7 on 2019-11-24 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Entry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
