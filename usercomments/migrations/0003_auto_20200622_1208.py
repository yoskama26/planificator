# Generated by Django 2.2.5 on 2020-06-22 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usercomments', '0002_auto_20200618_1325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='comment',
            name='hours',
            field=models.TimeField(default='0:00 AM'),
        ),
    ]