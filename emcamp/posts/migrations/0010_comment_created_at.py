# Generated by Django 3.0.2 on 2020-07-16 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20200716_0309'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
