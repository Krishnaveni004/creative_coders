# Generated by Django 2.1.1 on 2018-09-29 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codemania_app', '0003_auto_20180929_1235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test_form',
            old_name='cln',
            new_name='college',
        ),
        migrations.RenameField(
            model_name='test_form',
            old_name='cnt',
            new_name='contact',
        ),
    ]
