# Generated by Django 4.1.5 on 2023-09-14 10:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0008_alter_company_contact_person"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="contact_person",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
