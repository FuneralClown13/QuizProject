from django.forms import model_to_dict

from .models import Quiz, Question
from .serializers import QuestionSerializer


class QuizInfo:
    """
    Класс для получения аналитики по викторине
    """

    def __init__(self, quiz):
        self.quiz = quiz

    def get_count_quiz_passes(self):
        """
        Количество прохождений теста
        """
        instance = Quiz.objects.get(pk=self.quiz)
        return instance.passes

    def get_quiz_success_rate(self):
        """
        Процент успешного прохождения теста
        """
        instance = Quiz.objects.get(pk=self.quiz)
        data = model_to_dict(instance)
        return data['correct_passes'] / (data['passes'] or 1)

    def get_difficult_question(self):
        """
        Самый сложный вопрос в тесте
        """
        instance = Question.objects.filter(quiz=self.quiz)
        data = QuestionSerializer(instance, many=True).data

        result = 1
        result_id = 1

        for d in data:

            r = d['correct_passes'] / (d['passes'] or 1)
            if r < result:
                result = r
                result_id = d['id']

        r = QuestionSerializer(Question.objects.get(pk=result_id)).data
        r['per'] = result
        return r
