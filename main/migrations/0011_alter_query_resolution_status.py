# Generated by Django 5.0.1 on 2024-03-07 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_query_resolution_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='resolution_status',
            field=models.CharField(choices=[('DECLINED', 'Declined'), ('PENDING', 'Pending'), ('RESOLVED', 'Resolved'), ('IN_PROGRESS', 'In Progress')], max_length=20),
        ),
    ]