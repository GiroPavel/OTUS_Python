# Generated by Django 3.1.4 on 2021-01-09 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0021_auto_20210109_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clean',
            name='count_rooms',
        ),
    ]
