# Generated by Django 4.2.5 on 2023-10-31 05:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0004_rename_tenant_employee"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tenant",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name="Employee",
        ),
    ]
