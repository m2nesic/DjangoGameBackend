# Generated by Django 3.2.3 on 2021-06-20 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_alter_game_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='gold_average',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
    ]
