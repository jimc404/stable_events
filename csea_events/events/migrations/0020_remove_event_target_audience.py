# Generated by Django 2.2 on 2019-04-20 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0019_vote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='target_audience',
        ),
    ]
