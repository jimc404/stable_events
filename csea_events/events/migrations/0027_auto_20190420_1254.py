# Generated by Django 2.2 on 2019-04-20 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0026_auto_20190420_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventfeedback',
            name='rating',
            field=models.FloatField(),
        ),
    ]
