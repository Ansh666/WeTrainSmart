# Generated by Django 4.2.5 on 2024-07-05 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_customuser_session_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('user', 'User'), ('trainer', 'Trainer')], default='user', max_length=50),
        ),
    ]
