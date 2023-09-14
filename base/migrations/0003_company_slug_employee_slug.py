# Generated by Django 4.1.5 on 2023-09-14 06:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0002_alter_employee_employee_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="slug",
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="employee",
            name="slug",
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]