# Generated by Django 5.0.1 on 2024-02-28 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_course_classschedule_facilator_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classschedule',
            old_name='facilator',
            new_name='facilitator',
        ),
        migrations.AlterField(
            model_name='query',
            name='resolution_status',
            field=models.CharField(choices=[('IN_PROGRESS', 'In Progress'), ('DECLINED', 'Declined'), ('RESOLVED', 'Resolved'), ('PENDING', 'Pending')], max_length=20),
        ),
    ]
