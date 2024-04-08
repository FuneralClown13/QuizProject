# Generated by Django 5.0.4 on 2024-04-07 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_rename_text_answer_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='correct_passes',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='passes',
        ),
        migrations.AddField(
            model_name='question',
            name='correct_passes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='passes',
            field=models.IntegerField(default=0),
        ),
    ]