# Generated by Django 3.0.2 on 2020-07-13 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_remove_post_question_html'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='question',
            field=models.CharField(max_length=255),
        ),
    ]
