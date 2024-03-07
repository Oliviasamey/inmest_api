# Generated by Django 5.0.1 on 2024-03-07 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_delete_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='imuser',
            name='is_blocked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='imuser',
            name='permanent_login_fail',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='imuser',
            name='temporal_login_fail',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
