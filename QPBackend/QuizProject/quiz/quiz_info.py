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
        questions = QuestionSerializer(instance, many=True).data

        success_rate = 1
        difficult_question_id = 1

        for q in questions:

            q_success_rate = q['correct_passes'] / (q['passes'] or 1)
            if q_success_rate < success_rate:
                success_rate = q_success_rate
                difficult_question_id = q['id']

        difficult_question = QuestionSerializer(Question.objects.get(pk=difficult_question_id)).data
        difficult_question['per'] = success_rate
        return difficult_question
