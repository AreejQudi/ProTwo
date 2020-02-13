# Generated by Django 3.0.3 on 2020-02-13 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp',
            name='desc',
            field=models.TextField(default=1, max_length=1000, verbose_name='Description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emp',
            name='img',
            field=models.ImageField(default=1, upload_to='', verbose_name='img'),
            preserve_default=False,
        ),
    ]
