# Generated by Django 3.1.3 on 2020-11-23 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0005_note_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='public',
            field=models.BooleanField(default=False, verbose_name='公開'),
        ),
    ]
