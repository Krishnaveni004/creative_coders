# Generated by Django 2.1.7 on 2019-03-02 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codemania_app', '0038_patient_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_table',
            name='uid',
            field=models.CharField(default='aadhaar', max_length=12),
        ),
    ]
