# Generated by Django 5.0.4 on 2024-04-07 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_rename_quiz_passes_quiz_passes'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='correct_passes',
            field=models.IntegerField(default=0),
        ),
    ]