# Generated by Django 3.1.4 on 2021-01-07 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0014_auto_20210107_2313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clean',
            name='count_rooms',
        ),
    ]
