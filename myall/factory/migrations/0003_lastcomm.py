# Generated by Django 2.0.6 on 2019-01-28 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factory', '0002_auto_20180702_1327'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lastcomm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_ip', models.CharField(max_length=20)),
                ('timestame', models.IntegerField()),
            ],
        ),
    ]
