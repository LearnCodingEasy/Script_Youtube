# Generated by Django 5.0.6 on 2024-10-10 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('script', '0003_rename_list_of_sources_script_list_of_sources_urls'),
    ]

    operations = [
        migrations.AddField(
            model_name='script',
            name='list_of_fonts_urls',
            field=models.JSONField(default=list),
        ),
    ]