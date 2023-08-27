# Generated by Django 3.0.5 on 2023-08-25 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0017_auto_20230825_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.CharField(default='Recived', max_length=30),
        ),
        migrations.AddField(
            model_name='issuedbook',
            name='issued_by',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='issuedbook',
            name='status',
            field=models.CharField(default='Recived', max_length=20),
        ),
    ]