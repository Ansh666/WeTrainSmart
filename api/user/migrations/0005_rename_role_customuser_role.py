# Generated by Django 4.2.5 on 2024-07-20 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='ROLE',
            new_name='role',
        ),
    ]
