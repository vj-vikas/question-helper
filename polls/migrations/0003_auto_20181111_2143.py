# Generated by Django 2.1.2 on 2018-11-11 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='question',
            new_name='poll',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='votes',
        ),
    ]
