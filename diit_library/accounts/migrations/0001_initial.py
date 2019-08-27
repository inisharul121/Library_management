# Generated by Django 2.2.3 on 2019-08-20 09:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('full_name', models.CharField(max_length=15)),
                ('batch', models.IntegerField(blank=True, null=True)),
                ('class_id', models.IntegerField(blank=True, null=True, unique=True)),
                ('department', models.CharField(max_length=15)),
                ('id_card_number', models.CharField(max_length=15, unique=True)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('designation', models.CharField(max_length=15)),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
            ],
        ),
    ]
