# Generated by Django 3.0.5 on 2023-08-26 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0021_auto_20230826_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='requested_by',
            field=models.CharField(default='none', max_length=40),
        ),
    ]