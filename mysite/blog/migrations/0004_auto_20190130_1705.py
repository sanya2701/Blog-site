# Generated by Django 2.1.5 on 2019-01-30 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190130_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='comment',
            name='desc',
            field=models.TextField(max_length=500),
        ),
    ]
