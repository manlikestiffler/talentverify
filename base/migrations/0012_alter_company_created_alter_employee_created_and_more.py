# Generated by Django 4.1.5 on 2023-09-14 20:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0011_alter_company_created_alter_company_reg_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="created",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="employee",
            name="created",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="employee",
            name="date_employed",
            field=models.DateField(),
        ),
    ]