# Generated by Django 2.0.6 on 2019-01-29 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factory', '0004_auto_20190129_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diskdata',
            name='disk_free',
            field=models.IntegerField(),
        ),
    ]
