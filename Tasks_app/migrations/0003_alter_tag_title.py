# Generated by Django 3.2.9 on 2021-11-18 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks_app', '0002_remove_tag_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]