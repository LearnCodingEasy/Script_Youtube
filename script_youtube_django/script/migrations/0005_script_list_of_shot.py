# Generated by Django 5.0.6 on 2024-10-10 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('script', '0004_script_list_of_fonts_urls'),
    ]

    operations = [
        migrations.AddField(
            model_name='script',
            name='list_of_shot',
            field=models.JSONField(default=list),
        ),
    ]