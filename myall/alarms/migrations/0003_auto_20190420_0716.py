# Generated by Django 2.0.6 on 2019-04-20 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alarms', '0002_auto_20190420_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='threvalue',
            name='cpu_thre',
            field=models.FloatField(default=False),
        ),
        migrations.AlterField(
            model_name='threvalue',
            name='disk_thre',
            field=models.BigIntegerField(default=False),
        ),
        migrations.AlterField(
            model_name='threvalue',
            name='memory_thre',
            field=models.IntegerField(default=False),
        ),
    ]
