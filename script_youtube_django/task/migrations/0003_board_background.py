# Generated by Django 5.1.1 on 2024-11-03 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_board_card_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='background',
            field=models.CharField(default='#FFFFFF', max_length=100),
        ),
    ]