# Generated by Django 5.0.4 on 2024-04-07 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_answer_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='text',
            new_name='answer',
        ),
    ]
