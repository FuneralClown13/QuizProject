from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('quiz/', quiz, name='quiz'),
    path('questions/<int:quiz_id>/', questions, name='questions'),

    path('quiz_change/', quiz_change, name='quiz_change'),
    path('quiz_create', quiz_create, name='quiz_create'),
    path('quiz_update/<int:quiz_id>', quiz_update, name='quiz_update'),
    path('quiz_delete/<int:quiz_id>', quiz_delete, name='quiz_delete'),

    path('question_change/<int:quiz_id>', question_change, name='question_change'),
    path('question_create', question_create, name='question_create'),
    path('question_create/<int:quiz_id>', question_create, name='question_create'),
    path('question_delete/<int:quiz_id>/<int:question_id>', question_delete, name='question_delete'),

    path('result/<quiz_id>/', result, name='result'),
    path('submit_responses', submit_responses, name='submit_responses'),
]
