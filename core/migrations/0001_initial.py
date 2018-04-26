# Generated by Django 2.0.3 on 2018-04-26 09:54

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=core.models.md5hash_filename)),
                ('mime', models.CharField(blank=True, max_length=32)),
                ('file_hash', models.CharField(blank=True, max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('text', models.CharField(blank=True, db_index=True, max_length=1024)),
                ('readed_by', models.TextField(validators=[core.models.space_separated])),
                ('edited', models.BooleanField(default=False)),
                ('files', models.ManyToManyField(blank=True, to='core.File')),
                ('forwarded', models.ManyToManyField(blank=True, to='core.Message')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(blank=True, max_length=128)),
                ('bio', models.CharField(blank=True, max_length=128)),
                ('last_activity', models.DateTimeField(default=django.utils.timezone.now)),
                ('avatar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.File')),
                ('friend_requests', models.ManyToManyField(blank=True, to='core.Profile')),
                ('friends', models.ManyToManyField(blank=True, related_name='_profile_friends_+', to='core.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Puddle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=128)),
                ('avatar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.File')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator', to='core.Profile')),
                ('messages', models.ManyToManyField(blank=True, to='core.Message')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='puddles',
            field=models.ManyToManyField(blank=True, to='core.Puddle'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='message',
            name='hidden_from',
            field=models.ManyToManyField(blank=True, related_name='hidden_from', to='core.Profile'),
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Profile'),
        ),
        migrations.AddField(
            model_name='message',
            name='target_puddle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Puddle'),
        ),
        migrations.AddField(
            model_name='file',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Profile'),
        ),
    ]
