# Generated by Django 3.2 on 2021-06-27 23:55

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
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('edited', models.DateTimeField(auto_now=True, verbose_name='date edited')),
                ('is_edited', models.BooleanField(default=False, verbose_name='has post been edited')),
                ('text_ru', models.TextField(verbose_name='russian text')),
                ('text_en', models.TextField(blank=True, null=True, verbose_name='english text')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-published',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('text', models.TextField(verbose_name='text')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='notes.note')),
            ],
            options={
                'ordering': ('-published',),
            },
        ),
    ]
