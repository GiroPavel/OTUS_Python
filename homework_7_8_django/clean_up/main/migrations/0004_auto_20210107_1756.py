# Generated by Django 3.1.4 on 2021-01-07 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210107_0023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='name1',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='typeclean',
            old_name='name2',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='clean',
            name='countrooms',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='clean',
            name='place',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='clean',
            name='typeclean',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='clean',
            name='typyrooms',
            field=models.CharField(max_length=64),
        ),
    ]
