# Generated by Django 3.1.3 on 2020-11-05 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_auto_20201106_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='追加日時'),
        ),
        migrations.AlterField(
            model_name='note',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='更新日時'),
        ),
    ]
