"""
URL configuration for quizproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from quiz.views import QuestionViewSet, QuizViewSet, QuizInfoAPIView, QuizQuestionAPIView, AnswersApiView
from rest_framework import routers
router_quiz = routers.SimpleRouter()
router_question = routers.SimpleRouter()
router_quiz.register(r'quiz', QuizViewSet)
router_question.register(r'question', QuestionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router_quiz.urls)),
    path('api/v1/', include(router_question.urls)),

    path('api/v1/quizinfo/<int:quiz>/', QuizInfoAPIView.as_view()),

    path('api/v1/quizquestions/', QuizQuestionAPIView.as_view()),
    path('api/v1/quizquestions/<int:quiz>/', QuizQuestionAPIView.as_view()),
    #
    path('api/v1/answers/', AnswersApiView.as_view()),

]
