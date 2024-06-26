# Generated by Django 4.2.11 on 2024-04-11 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0010_alter_productcategorymodel_slug_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="productcategorymodel",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="children",
                to="shop.productcategorymodel",
                verbose_name="parent",
            ),
        ),
        migrations.AlterField(
            model_name="productmodel",
            name="status",
            field=models.IntegerField(
                choices=[(1, "show"), (2, "dontshow")], default=2
            ),
        ),
    ]
