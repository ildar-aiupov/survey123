# Generated by Django 5.0.1 on 2024-02-02 17:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Done_answer",
            new_name="Answer",
        ),
        migrations.AlterField(
            model_name="question",
            name="survey",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="questions",
                to="main.survey",
            ),
        ),
        migrations.AlterField(
            model_name="variant",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="variants",
                to="main.question",
            ),
        ),
    ]
