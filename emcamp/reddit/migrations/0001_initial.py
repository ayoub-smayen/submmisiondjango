# Generated by Django 2.1 on 2021-07-28 21:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=12)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('ups', models.IntegerField(default=0)),
                ('downs', models.IntegerField(default=0)),
                ('score', models.IntegerField(default=0)),
                ('raw_comment', models.TextField(blank=True)),
                ('html_comment', models.TextField(blank=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.RedditUser')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='reddit.Comment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=12)),
                ('title', models.CharField(max_length=250)),
                ('url', models.URLField(blank=True, null=True)),
                ('text', models.TextField(blank=True, max_length=5000)),
                ('text_html', models.TextField(blank=True)),
                ('ups', models.IntegerField(default=0)),
                ('downs', models.IntegerField(default=0)),
                ('score', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment_count', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.RedditUser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_object_id', models.PositiveIntegerField()),
                ('value', models.IntegerField(default=0)),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reddit.Submission')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.RedditUser')),
                ('vote_object_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='submission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reddit.Submission'),
        ),
    ]
