from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    passes = models.IntegerField(default=0)
    correct_passes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.CharField(max_length=255)
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE, null=True)
    correct_answer = models.TextField(blank=True)
    passes = models.IntegerField(default=0)
    correct_passes = models.IntegerField(default=0)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text


class Answer(models.Model):
    answer = models.CharField(max_length=255, null=True)
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE, null=True)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.answer
