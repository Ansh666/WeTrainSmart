# Generated by Django 4.2.5 on 2024-07-22 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_rename_role_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='name',
            field=models.CharField(default='Name', max_length=50),
        ),
    ]
