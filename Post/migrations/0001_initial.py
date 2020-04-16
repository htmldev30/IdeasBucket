# Generated by Django 3.0.5 on 2020-04-16 05:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Communities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community_name', models.CharField(max_length=25, null=True)),
                ('community_bio', models.CharField(max_length=100, null=True)),
                ('community_image_icon', models.FileField(default='/community_icons/default_community_icon.jpg', null=True, upload_to='community_icons')),
                ('community_created_time', models.DateTimeField(auto_now_add=True)),
                ('community_slug', models.SlugField(max_length=40, unique=True)),
                ('user_created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Communities',
            },
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idea', models.CharField(max_length=25, null=True)),
                ('is_public', models.BooleanField(default=False)),
                ('time_posted', models.DateTimeField(auto_now_add=True)),
                ('to_community', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Post.Communities')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
