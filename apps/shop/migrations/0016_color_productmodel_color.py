# Generated by Django 4.2.11 on 2024-04-13 08:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0015_alter_productcomment_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Color",
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
                ("title", models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name="productmodel",
            name="color",
            field=models.ManyToManyField(related_name="products", to="shop.color"),
        ),
    ]
