# Generated by Django 2.2.10 on 2021-02-16 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='height',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='picture',
            name='width',
            field=models.IntegerField(blank=True),
        ),
    ]
