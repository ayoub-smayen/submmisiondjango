# Generated by Django 3.0.2 on 2020-07-16 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_comment_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.ImageField(blank=True, upload_to='pics'),
        ),
    ]
