# Generated by Django 3.2.4 on 2021-07-13 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='preview',
            field=models.CharField(blank=True, max_length=200, verbose_name='post title'),
        ),
    ]
