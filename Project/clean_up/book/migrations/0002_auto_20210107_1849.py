# Generated by Django 3.1.4 on 2021-01-07 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='countrooms',
            name='place',
        ),
        migrations.AddField(
            model_name='countrooms',
            name='name',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
    ]
