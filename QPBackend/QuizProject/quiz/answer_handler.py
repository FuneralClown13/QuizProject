from django.forms import model_to_dict

from .models import Quiz, Question
from .serializers import QuizSerializer, QuestionSerializer


class AnswerResultProcessor:
    """
    Класс для обработки полученных ответов
    """

    def __init__(self, data: dict):
        self.data = data
        self.quiz = data.get('quiz', None)
        self.question = None

        self.answer = None
        self.answers = 0
        self.correct_answers = 0

    def execute(self):
        """
        Общий метод для последовательного выполнения методов класса
        """
        for data in self.data['answers']:
            self.answer = data.get('answer', None)
            self.question = data.get('question', None)
            if self.question:
                self.__update_question_passes()

        if self.quiz:
            self.__update_quiz_passes()
            if (self.correct_answers / self.answers) >= 0.5:
                self.__update_quiz_success_rate()

    def __get_instance_and_data(self, model, pk):
        """
        Получение объектов instance и data
        """
        instance = model.objects.get(pk=pk)
        data = model_to_dict(instance)
        return instance, data

    def __ex_serializer(self, serializer_cls, data, instance):
        """
        Проверка и запись данных в бд
        """
        serializer = serializer_cls(data=data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def __update_quiz_passes(self):
        """
        Обновление счетчика кол-ва прохождений викторины
        """
        instance, data = self.__get_instance_and_data(Quiz, self.quiz)
        data['passes'] += 1
        self.__ex_serializer(QuizSerializer, data, instance)

    def __update_question_passes(self):
        """
        Обновление счетчика кол-ва прохождений вопроса
        Обновление счетчика кол-ва правильных ответов на вопрос
        """
        instance, data = self.__get_instance_and_data(Question, self.question)

        data['passes'] += 1
        self.answers += 1
        if self.answer.lower() == data['correct_answer'].lower():
            data['correct_passes'] += 1
            self.correct_answers += 1

        self.__ex_serializer(QuestionSerializer, data, instance)

    def __update_quiz_success_rate(self):
        """
        Обновление счетчика кол-ва успешных прохождений викторины
        """
        instance, data = self.__get_instance_and_data(Quiz, self.quiz)
        data['correct_passes'] += 1
        self.__ex_serializer(QuizSerializer, data, instance)
