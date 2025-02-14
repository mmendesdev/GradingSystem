# Generated by Django 5.0.6 on 2024-07-25 14:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notas", "0002_alter_nota_titulo"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="nota",
            options={"verbose_name": "Note", "verbose_name_plural": "Notes"},
        ),
        migrations.AlterField(
            model_name="nota",
            name="categoria",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="notas.categoria",
                verbose_name="Category",
            ),
        ),
        migrations.AlterField(
            model_name="nota",
            name="conteudo",
            field=models.TextField(verbose_name="Content"),
        ),
        migrations.AlterField(
            model_name="nota",
            name="criado_em",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Created in"),
        ),
        migrations.AlterField(
            model_name="nota",
            name="titulo",
            field=models.CharField(max_length=100, verbose_name="Note title"),
        ),
        migrations.AlterField(
            model_name="nota",
            name="usuario",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Owner",
            ),
        ),
    ]
