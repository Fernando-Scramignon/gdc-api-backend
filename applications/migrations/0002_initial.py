<<<<<<< HEAD
# Generated by Django 4.1.2 on 2022-11-04 13:02
=======
# Generated by Django 4.1.2 on 2022-11-04 04:54
>>>>>>> development

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("applications", "0001_initial"),
=======
        ("applications", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
>>>>>>> development
    ]

    operations = [
        migrations.AddField(
            model_name="application",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="applications",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
