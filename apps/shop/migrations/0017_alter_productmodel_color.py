# Generated by Django 4.2.11 on 2024-04-13 08:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0016_color_productmodel_color"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productmodel",
            name="color",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="products", to="shop.color"
            ),
        ),
    ]