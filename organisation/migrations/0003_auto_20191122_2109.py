# Generated by Django 2.2.5 on 2019-11-22 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0002_auto_20191122_2106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collaborator',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='collaborator',
            name='last_name',
        ),
    ]
