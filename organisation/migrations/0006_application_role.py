# Generated by Django 2.2.5 on 2019-11-23 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0005_direction_shorname'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organisation.Role'),
        ),
    ]