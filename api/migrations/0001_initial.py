from django.db import migrations
from api.user.models import CustomUser


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name="Ayush", email="wetrainsmart@gmail.com",
                          is_staff=True,
                          is_superuser=True,
                          phone="987156487",
                          gender="Male"
                          )

        user.set_password("1234")
        user.save()

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.RunPython(seed_data), ]
