# Generated by Django 2.1.1 on 2018-11-05 12:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('codemania_app', '0021_auto_20181103_0926'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataVirtualizationForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=100)),
                ('parent_contact', models.CharField(default='parent_contact', max_length=100)),
                ('email', models.EmailField(default='email', max_length=100)),
                ('contact', models.CharField(default='phone', max_length=100)),
                ('add', models.CharField(default='address', max_length=100)),
                ('college', models.CharField(default='college', max_length=100)),
                ('cty_l', models.CharField(default='current_city', max_length=100)),
                ('review', models.CharField(default='review', max_length=100)),
                ('review_message', models.CharField(default='review message', max_length=500)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
