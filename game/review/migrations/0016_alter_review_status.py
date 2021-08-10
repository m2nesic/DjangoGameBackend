# Generated by Django 3.2.3 on 2021-06-20 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0015_alter_review_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10),
        ),
    ]
