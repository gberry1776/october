# Generated by Django 3.0.3 on 2020-05-17 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_auto_20200517_1706'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='groupmember',
            options={'permissions': (('can_drive', 'can take jobs'),)},
        ),
    ]
