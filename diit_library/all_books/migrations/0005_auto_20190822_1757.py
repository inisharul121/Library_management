# Generated by Django 2.2.3 on 2019-08-22 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_books', '0004_auto_20190822_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='borrow',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='borrow',
            name='is_returned',
            field=models.BooleanField(default=False),
        ),
    ]
