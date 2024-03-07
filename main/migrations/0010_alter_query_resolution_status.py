# Generated by Django 5.0.1 on 2024-03-07 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_query_resolution_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='resolution_status',
            field=models.CharField(choices=[('RESOLVED', 'Resolved'), ('DECLINED', 'Declined'), ('PENDING', 'Pending'), ('IN_PROGRESS', 'In Progress')], max_length=20),
        ),
    ]
