# Generated by Django 3.0.3 on 2020-05-18 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_auto_20200517_1729'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='groupmember',
            options={},
        ),
    ]
