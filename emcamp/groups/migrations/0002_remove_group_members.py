# Generated by Django 3.0.2 on 2020-07-09 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='members',
        ),
    ]