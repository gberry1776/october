# Generated by Django 3.0.3 on 2020-07-10 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0002_auto_20200703_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='egroup',
            name='goldinroom',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='goldinroom'),
        ),
    ]
