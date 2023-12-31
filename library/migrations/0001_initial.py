# Generated by Django 4.2.5 on 2023-09-08 09:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import library.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentExtra',
            fields=[
                ('my_primary_key', models.BigAutoField(primary_key=True, serialize=False)),
                ('student_id', models.CharField(max_length=40, unique=True)),
                ('department_name', models.CharField(default='Unknown Department', max_length=100)),
                ('session', models.CharField(default='', max_length=20)),
                ('educational_year', models.PositiveIntegerField(default=2023)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IssuedBook',
            fields=[
                ('my_primary_key', models.BigAutoField(primary_key=True, serialize=False)),
                ('student_id', models.CharField(max_length=30)),
                ('isbn', models.CharField(max_length=30)),
                ('issuedate', models.DateField(auto_now=True)),
                ('expirydate', models.DateField(default=library.models.get_expiry)),
                ('department_name', models.CharField(default='Unknown Department', max_length=100)),
                ('session', models.CharField(default='', max_length=20)),
                ('educational_year', models.PositiveIntegerField(default=2023)),
                ('issued_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('my_primary_key', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('isbn', models.PositiveIntegerField()),
                ('author', models.CharField(max_length=40)),
                ('category', models.CharField(choices=[('education', 'Education'), ('entertainment', 'Entertainment'), ('comics', 'Comics'), ('biography', 'Biography'), ('history', 'History'), ('novel', 'Novel'), ('fantasy', 'Fantasy'), ('thriller', 'Thriller'), ('romance', 'Romance'), ('scifi', 'Sci-Fi')], default='education', max_length=30)),
                ('publication_name', models.CharField(blank=True, max_length=50)),
                ('publication_date', models.DateField(blank=True, null=True)),
                ('edition', models.PositiveIntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('received', 'Received'), ('issued', 'Issued'), ('pending', 'Pending'), ('return_requested', 'Return_Requested')], default='received', max_length=20)),
                ('requested_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.studentextra')),
            ],
        ),
    ]
