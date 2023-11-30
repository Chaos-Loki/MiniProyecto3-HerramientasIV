# Generated by Django 4.2.5 on 2023-11-25 10:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_category_product_userprofile_role_review"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="role",
            field=models.CharField(
                blank=True,
                choices=[("cliente", "Cliente"), ("vendedor", "Vendedor")],
                default="",
                max_length=20,
            ),
        ),
    ]