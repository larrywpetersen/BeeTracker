# Generated by Django 2.1.5 on 2019-01-30 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hives', '0002_auto_20190128_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='hive',
            name='date_entered',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
