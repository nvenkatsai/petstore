# Generated by Django 5.0.4 on 2024-06-05 11:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ecomapp", "0015_alter_product_cat"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="cat",
            field=models.IntegerField(
                choices=[
                    (1, "Beagle"),
                    (2, "Bulldog"),
                    (3, "German Shepherd"),
                    (4, "Poddle"),
                    (5, "English Springer Spaniel"),
                    (6, "Airedale Terrier"),
                ],
                verbose_name="Category",
            ),
        ),
    ]