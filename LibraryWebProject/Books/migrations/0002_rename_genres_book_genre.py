# Generated by Django 4.2.7 on 2023-12-04 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='genres',
            new_name='genre',
        ),
    ]
