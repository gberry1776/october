# Generated by Django 3.0.3 on 2020-08-03 07:57

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('experiment', '0008_auto_20200730_1118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='isjudge',
            old_name='judge',
            new_name='judge1',
        ),
        migrations.AlterUniqueTogether(
            name='isjudge',
            unique_together={('courtroom', 'judge1')},
        ),
    ]