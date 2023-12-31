# Generated by Django 4.1.5 on 2023-09-14 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0005_delete_roles_employee_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="company",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="base.company",
            ),
        ),
    ]
