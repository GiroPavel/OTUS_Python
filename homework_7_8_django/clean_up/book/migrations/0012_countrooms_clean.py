# Generated by Django 3.1.4 on 2021-01-07 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0011_auto_20210107_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='countrooms',
            name='clean',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='book.clean'),
            preserve_default=False,
        ),
    ]
