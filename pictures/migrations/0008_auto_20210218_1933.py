# Generated by Django 2.2.10 on 2021-02-18 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0007_auto_20210216_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='base_height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='picture',
            name='base_width',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
