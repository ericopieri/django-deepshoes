# Generated by Django 4.1 on 2022-09-12 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ped_pro",
            name="pedido",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="core.pedido"
            ),
        ),
        migrations.AlterField(
            model_name="ped_pro",
            name="produto",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="core.produto"
            ),
        ),
    ]
