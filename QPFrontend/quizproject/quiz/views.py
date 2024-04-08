from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests
from django.views.decorators.csrf import requires_csrf_token, csrf_exempt
from django.views.generic import ListView
from .response_answers import ResponseAnswers


def index(request):
    response = requests.get('http://127.0.0.1:4000/api/v1/quiz/')
    quiz = response.json()
    return render(request, 'quiz/index.html'
                  , {'title': 'Index', 'quiz': quiz})


def about(request):
    return render(request, 'quiz/about.html',
                  {'title': 'about'})


def quiz(request):
    response = requests.get('http://127.0.0.1:4000/api/v1/quiz/')
    quiz_data = response.json()
    return render(request, 'quiz/quiz.html'
                  , {'title': 'Quiz', 'quiz': quiz_data[::-1]})


def quiz_change(request):
    response = requests.get('http://127.0.0.1:4000/api/v1/quiz/')
    quiz_data = response.json()
    return render(request, 'quiz/quiz_change.html'
                  , {'title': 'Quiz', 'quiz': quiz_data[::-1]})


@csrf_exempt
def quiz_create(request):
    if request.POST:
        json_data = {'title': request.POST['title'], 'description': request.POST['description']}
        requests.post('http://127.0.0.1:4000/api/v1/quiz/', json=json_data)
        return redirect('quiz_change/')

    return render(request, 'quiz/quiz_create.html'
                  , {'title': 'QuizCreate'})


@csrf_exempt
def quiz_update(request, quiz_id):
    if request.POST:
        json_data = {'title': request.POST['title'], 'description': request.POST['description']}
        print(json_data, quiz_id)
        requests.put(f'http://127.0.0.1:4000/api/v1/quiz/{quiz_id}/', json=json_data)
        return redirect(quiz_change)

    response = requests.get(f'http://127.0.0.1:4000/api/v1/quiz/{quiz_id}/')
    quiz_data = response.json()
    return render(request, 'quiz/quiz_update.html'
                  , {'title': 'QuizUpdate', 'quiz': quiz_data})


def quiz_delete(request, quiz_id):
    requests.delete(f'http://127.0.0.1:4000/api/v1/quiz/{quiz_id}/')
    return redirect(quiz_change)


def questions(request, quiz_id=1):
    response = requests.get(f'http://127.0.0.1:4000/api/v1/quizquestions/{quiz_id}/')
    questions_data = response.json()
    return render(request, 'quiz/questions.html'
                  , {'title': 'Questions', 'quiz_id': quiz_id, 'questions': questions_data[f'questions']})


@csrf_exempt
def question_change(request, quiz_id=1):
    response = requests.get(f'http://127.0.0.1:4000/api/v1/quizquestions/{quiz_id}/')
    questions_data = response.json()
    return render(request, 'quiz/questions_change.html'
                  , {'title': 'QuestionsChange', 'quiz_id': quiz_id, 'questions': questions_data[f'questions']})


@csrf_exempt
def question_create(request, quiz_id=2):
    if request.POST:
        json_data = {'text': request.POST['text'], 'correct_answer': request.POST['correct_answer'], 'quiz': quiz_id}
        requests.post('http://127.0.0.1:4000/api/v1/question/', json=json_data)
        return redirect(question_change, quiz_id=quiz_id)

    return render(request, 'quiz/question_create.html'
                  , {'title': 'QuestionCreate', 'quiz_id': quiz_id})


def question_delete(request, quiz_id, question_id):
    requests.delete(f'http://127.0.0.1:4000/api/v1/question/{question_id}/')
    return redirect(question_change, quiz_id=quiz_id)


def result(request, quiz_id):
    response = requests.get(f'http://127.0.0.1:4000/api/v1/quizinfo/{quiz_id}/')
    quizinfo_data = response.json()
    return render(request, 'quiz/quizinf.html'
                  , {'title': 'QuizInfo', 'quiz_info': quizinfo_data['quiz_info']})


@csrf_exempt
def submit_responses(request):
    if request.POST:
        answers = ResponseAnswers(request.POST)
        answers.execute()
        return redirect(f'result/{request.POST['quiz_id']}')

    return redirect('quiz/')
