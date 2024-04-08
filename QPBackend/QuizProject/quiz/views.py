from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Quiz, Question, Answer
from .serializers import QuizSerializer, QuestionSerializer, AnswerSerializer
from .answer_handler import AnswerResultProcessor
from .quiz_info import QuizInfo


class QuizViewSet(viewsets.ModelViewSet):
    """
    Класс-представление для опросов
    """
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """
    Класс-представление для вопросов тестов
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswersApiView(generics.ListAPIView):
    """
    Класс-представление для ответов на вопросы
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def post(self, request):
        """
        записывает ответы в бд
        затем запускает обработку ответов
        """
        answer_list = []
        data_dict = {
            "quiz": request.data['quiz'],
            "answers": answer_list
        }
        for data in request.data['answers']:
            serializer = AnswerSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            answer_list.append(serializer.data)
        try:
            answer_handler = AnswerResultProcessor(data_dict)
            answer_handler.execute()
        except:
            return Response({'error': 'Object does not exists'})

        return Response({'request': answer_list})


class QuizInfoAPIView(APIView):
    """
    Класс-представление для получения аналитики по тесту
    """
    def get(self, request, quiz=1):
        quiz_info = QuizInfo(quiz)

        return Response({'quiz_info': {
            'count_quiz_passes': quiz_info.get_count_quiz_passes(),
            'difficult_question': quiz_info.get_difficult_question(),
            'success_rate': quiz_info.get_quiz_success_rate()
        }})


class QuizQuestionAPIView(APIView):
    """
    Класс-представление для получения списка вопросов определенного теста
    quiz: pk теста для получения вопросов
    """

    def get(self, request, quiz=1):
        lst = Question.objects.filter(quiz=quiz)
        return Response({'quiz': quiz,
                         'questions': QuestionSerializer(lst, many=True).data})
