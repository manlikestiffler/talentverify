# Generated by Django 4.1.5 on 2023-09-14 00:40

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
            name="Employee",
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
                ("employee_name", models.CharField(max_length=300)),
                ("employee_ID", models.FloatField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["-updated", "-created"],
            },
        ),
        migrations.CreateModel(
            name="Roles",
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
                ("department", models.CharField(max_length=200)),
                ("role_name", models.CharField(max_length=200)),
                ("date_started", models.DateTimeField()),
                ("date_ended", models.DateTimeField()),
                ("duties", models.TextField()),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["-created"],
            },
        ),
        migrations.CreateModel(
            name="Company",
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
                ("company_name", models.CharField(max_length=300)),
                ("reg_number", models.CharField(max_length=60)),
                ("reg_date", models.DateTimeField()),
                ("address", models.CharField(max_length=300)),
                ("departments", models.IntegerField(default="0")),
                ("contact", models.CharField(max_length=60)),
                ("email_address", models.EmailField(max_length=254)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "contact_person",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Companies",
                "ordering": ["-created"],
            },
        ),
    ]
