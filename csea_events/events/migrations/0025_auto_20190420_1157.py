# Generated by Django 2.2 on 2019-04-20 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0024_auto_20190420_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='venue',
            field=models.CharField(choices=[('Lecture Hall 1', 'Lecture Hall 1'), ('Lecture Hall 2', 'Lecture Hall 2'), ('Lecture Hall 3', 'Lecture Hall 3'), ('Lecture Hall 4', 'Lecture Hall 4'), ('Conference Room', 'Conference Room'), ('CSE Seminar Room', 'CSE Seminar Room'), ('Core 2 Rooms', 'Core 2 Rooms'), ('Core 5 Rooms', 'Core 5 Rooms'), ('Mini Auditorium', 'Mini Auditorium'), ('Main Auditorium', 'Main Auditorium'), ('Department Library', 'Department Library'), ('None', 'None')], default='CSE Seminar Room', max_length=50),
        ),
    ]