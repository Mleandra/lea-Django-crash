# Generated by Django 3.0 on 2020-03-05 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manga',
            old_name='mangaka',
            new_name='mangakas',
        ),
    ]