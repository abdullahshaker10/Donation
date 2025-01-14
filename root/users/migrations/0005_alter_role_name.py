# Generated by Django 5.1.4 on 2025-01-06 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_alter_user_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="role",
            name="name",
            field=models.CharField(
                choices=[
                    ("Admin", "ADMIN"),
                    ("Donar", "DONAR"),
                    ("Organizer", "ORGANIZER"),
                    ("Investor", "INVESTOR"),
                ],
                max_length=255,
                unique=True,
            ),
        ),
    ]
