# Generated by Django 2.1.7 on 2019-03-03 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codemania_app', '0043_auto_20190303_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_table',
            name='dname',
            field=models.CharField(default='dname', max_length=200),
        ),
        migrations.AddField(
            model_name='patient_table',
            name='hname',
            field=models.CharField(default='hname', max_length=200),
        ),
        migrations.AddField(
            model_name='patient_table',
            name='pname',
            field=models.CharField(default='pname', max_length=200),
        ),
    ]
