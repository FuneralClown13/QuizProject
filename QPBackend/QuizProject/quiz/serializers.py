from rest_framework import serializers

from .models import Quiz, Question, Answer


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id', 'title', 'description', 'passes', 'correct_passes')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'text', 'quiz', 'correct_answer', 'passes', 'correct_passes')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'answer', 'quiz', 'question')

