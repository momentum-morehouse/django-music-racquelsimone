# Generated by Django 3.0.8 on 2020-07-13 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymusic', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='albumtitle',
            new_name='album_title',
        ),
        migrations.RenameField(
            model_name='album',
            old_name='artistname',
            new_name='artist_name',
        ),
        migrations.RemoveField(
            model_name='album',
            name='released',
        ),
        migrations.AddField(
            model_name='album',
            name='date_released',
            field=models.DateField(blank=True, null=True),
        ),
    ]
