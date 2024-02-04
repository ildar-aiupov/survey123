# Generated by Django 5.0.1 on 2024-02-03 11:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_rename_done_answer_answer_alter_question_survey_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="QuestionSession",
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
                ("session", models.CharField(max_length=500, verbose_name="Сессия")),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.question"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SurveySession",
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
                ("session", models.CharField(max_length=500, verbose_name="Сессия")),
                (
                    "survey",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.survey"
                    ),
                ),
            ],
        ),
    ]