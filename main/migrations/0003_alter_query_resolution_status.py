# Generated by Django 5.0.1 on 2024-02-15 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='resolution_status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('DECLINED', 'Declined'), ('RESOLVED', 'Resolved'), ('IN_PROGRESS', 'In Progress')], max_length=20),
        ),
    ]