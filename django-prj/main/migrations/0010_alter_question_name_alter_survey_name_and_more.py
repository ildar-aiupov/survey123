# Generated by Django 5.0.1 on 2024-02-08 23:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0009_alter_answer_options_alter_question_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="name",
            field=models.CharField(max_length=500, verbose_name="Название вопроса"),
        ),
        migrations.AlterField(
            model_name="survey",
            name="name",
            field=models.CharField(max_length=500, verbose_name="Название опроса"),
        ),
        migrations.AlterField(
            model_name="variant",
            name="name",
            field=models.CharField(max_length=500, verbose_name="Название варианта"),
        ),
    ]
