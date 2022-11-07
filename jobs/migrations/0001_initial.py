from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("companies", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Job",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("url", models.CharField(max_length=254, unique=True)),
                ("title", models.CharField(max_length=127)),
                ("period", models.CharField(max_length=15)),
                ("location", models.CharField(max_length=30)),
                ("contract", models.CharField(max_length=15)),
                ("estimated_pay", models.PositiveIntegerField()),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("Estágio", "Intern"),
                            ("Treinee", "Trainee"),
                            ("Júnior", "Junior"),
                            ("Pleno", "Mid"),
                            ("Sênior", "Senior"),
                            ("Não definido", "Default"),
                        ],
                        default="Não definido",
                        max_length=15,
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Front-End", "Front"),
                            ("Back-End", "Back"),
                            ("Full-Stack", "Full"),
                            ("Não definido", "Default"),
                        ],
                        default="Não definido",
                        max_length=15,
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="jobs",
                        to="companies.company",
                    ),
                ),
            ],
        ),
    ]
