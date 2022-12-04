# Generated by Django 4.1 on 2022-12-04 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_remove_pedido_preco_total"),
    ]

    operations = [
        migrations.AddField(
            model_name="pedido",
            name="preco_final",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
