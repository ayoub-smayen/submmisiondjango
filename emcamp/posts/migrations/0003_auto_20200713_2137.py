# Generated by Django 3.0.2 on 2020-07-13 16:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_auto_20200713_2132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='message',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='message_html',
            new_name='question_html',
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together={('user', 'question')},
        ),
    ]
