# Generated by Django 2.0.6 on 2019-04-20 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alarms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='threvalue',
            name='thre_name',
        ),
        migrations.RemoveField(
            model_name='threvalue',
            name='thre_value',
        ),
        migrations.AddField(
            model_name='threvalue',
            name='cpu_thre',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='threvalue',
            name='disk_thre',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='threvalue',
            name='memory_thre',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
