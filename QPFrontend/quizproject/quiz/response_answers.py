import json

import requests


class ResponseAnswers:
    def __init__(self, request):
        self.request = request

    def execute(self):
        """
        Общий метод для последовательного выполнения методов класса
        """
        r = self.prepare_data()
        self.send_answers(r)

    def prepare_data(self):
        """
        Метод prepare_data формирует словарь r, содержащий идентификатор викторины и ответы на вопросы,
        которые извлекаются из self.request.
        """
        r = {"quiz": self.request['quiz_id'],
             "answers": [{"answer": self.request[q], "question": q} for q in self.request if q != 'quiz_id']
             }
        return r

    def send_answers(self, r):
        """
        Метод send_answers отправляет сформированные данные на указанный URL
        """
        resp = requests.post('http://127.0.0.1:4000/api/v1/answers/', json=r)
        return resp
