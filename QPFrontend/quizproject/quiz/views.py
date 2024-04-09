from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .response_answers import ResponseAnswers
from .qpbackend.qpbackend import QPBackend


def index(request):
    """
        Обработчик для главной страницы
    """
    quiz_data = QPBackend().get_quiz()

    return render(request, 'quiz/index.html'
                  , {'title': 'Index', 'quiz': quiz_data})


def about(request):
    """
        Обработчик для страницы about
    """
    return render(request, 'quiz/about.html',
                  {'title': 'about'})


def quiz(request):
    """
        Обработчик для списка тестов
    """
    quiz_data = QPBackend().get_quiz()

    return render(request, 'quiz/quiz.html'
                  , {'title': 'Quiz', 'quiz': quiz_data[::-1]})


def quiz_change(request):
    """
        Обработчик для страницы редактора тестов
    """
    quiz_data = QPBackend().get_quiz()
    return render(request, 'quiz/quiz_change.html'
                  , {'title': 'Quiz', 'quiz': quiz_data[::-1]})


@csrf_exempt
def quiz_create(request):
    """
        Обработчик создания теста
    """
    if request.POST:
        json_data = {'title': request.POST['title'], 'description': request.POST['description']}
        QPBackend().post_quiz(json_data)

        return redirect('quiz_change/')

    return render(request, 'quiz/quiz_create.html'
                  , {'title': 'QuizCreate'})


@csrf_exempt
def quiz_update(request, quiz_id):
    """
        Обработчик обновления теста
    """
    if request.POST:
        json_data = {'title': request.POST['title'], 'description': request.POST['description']}
        QPBackend(quiz_id).put_quiz(json_data)
        return redirect(quiz_change)

    quiz_data = QPBackend(quiz_id).get_quiz()
    return render(request, 'quiz/quiz_update.html'
                  , {'title': 'QuizUpdate', 'quiz': quiz_data})


def quiz_delete(request, quiz_id):
    """
            Обработчик удаления теста
    """
    QPBackend(quiz_id).delete_quiz()
    return redirect(quiz_change)


def questions(request, quiz_id=1):
    """
        Обработчик для страницы со списком вопросов теста pk = quiz_id
    """
    questions_data = QPBackend(quiz_id).get_quiz_questions()
    return render(request, 'quiz/questions.html'
                  , {'title': 'Questions', 'quiz_id': quiz_id, 'questions': questions_data[f'questions']})


@csrf_exempt
def question_change(request, quiz_id=1):
    """
        Обработчик для страницы редактора вопросов
    """
    questions_data = QPBackend(quiz_id).get_quiz_questions()
    return render(request, 'quiz/questions_change.html'
                  , {'title': 'QuestionsChange', 'quiz_id': quiz_id, 'questions': questions_data[f'questions']})


@csrf_exempt
def question_create(request, quiz_id=2):
    """
        Обработчик создания вопроса
    """
    if request.POST:
        json_data = {'text': request.POST['text'], 'correct_answer': request.POST['correct_answer'], 'quiz': quiz_id}
        QPBackend().post_question(json_data)
        return redirect(question_change, quiz_id=quiz_id)

    return render(request, 'quiz/question_create.html'
                  , {'title': 'QuestionCreate', 'quiz_id': quiz_id})


def question_delete(request, quiz_id, question_id):
    """
        Обработчик удаления вопроса
    """
    QPBackend(quiz_id).delete_question()
    return redirect(question_change, quiz_id=quiz_id)


def result(request, quiz_id):
    """
        Обработчик для страницы результатов/аналитики теста
    """
    quizinfo_data = QPBackend(quiz_id).get_quiz_info()
    return render(request, 'quiz/quizinf.html'
                  , {'title': 'QuizInfo', 'quiz_info': quizinfo_data['quiz_info']})


@csrf_exempt
def submit_responses(request):
    """
        Функция для подготовки и отправки на сервер

    """
    if request.POST:
        answers = ResponseAnswers(request.POST)
        answers.execute()
        return redirect(f'result/{request.POST['quiz_id']}')

    return redirect('quiz/')
