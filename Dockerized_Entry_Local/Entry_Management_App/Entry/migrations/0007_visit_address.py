# Generated by Django 2.2.7 on 2019-11-25 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Entry', '0006_auto_20191125_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='address',
            field=models.CharField(default='innovacer office', max_length=250),
            preserve_default=False,
        ),
    ]
