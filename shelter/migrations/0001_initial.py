# Generated by Django 4.1 on 2022-08-27 21:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Animal",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("animal_name", models.CharField(max_length=36)),
                (
                    "animal_type",
                    models.CharField(
                        choices=[
                            ("", ""),
                            ("Dog", "Dog"),
                            ("Cat", "Cat"),
                            ("Bird", "Bird"),
                            ("Rabbit", "Rabbit"),
                            ("Other", "Other"),
                        ],
                        default="",
                        max_length=16,
                    ),
                ),
                ("breed", models.CharField(max_length=32)),
                ("personality", models.TextField(default="")),
                ("cared_by", models.CharField(max_length=16)),
                (
                    "animal_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
