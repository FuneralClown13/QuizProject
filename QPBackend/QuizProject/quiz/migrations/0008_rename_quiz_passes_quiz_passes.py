# Generated by Django 5.0.4 on 2024-04-07 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_remove_answer_correct_passes_remove_answer_passes_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='quiz_passes',
            new_name='passes',
        ),
    ]