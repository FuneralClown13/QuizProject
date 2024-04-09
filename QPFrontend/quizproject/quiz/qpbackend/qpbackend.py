import requests
from .urls import get_url


class QPBackend:
    """
    Класс для взаимодействия с сервисом QPBackend
    """
    def __init__(self, id_=None):
        """
        :param id_: pk для quiz или question
        """
        self.id_ = id_

    def get_quiz(self):
        response = requests.get(get_url('quiz', self.id_))
        return response.json()

    def post_quiz(self, json_data):
        requests.post(get_url('quiz', self.id_), json=json_data)

    def put_quiz(self, json_data):
        requests.put(get_url('quiz', self.id_), json=json_data)

    def delete_quiz(self):
        requests.delete(get_url('quiz', self.id_))

    def get_quiz_questions(self):
        response = requests.get(get_url('quizquestions', self.id_))
        return response.json()

    def post_question(self, json_data):
        requests.post(get_url('question', self.id_), json=json_data)

    def delete_question(self):
        requests.delete(get_url('question', self.id_))

    def get_quiz_info(self):
        response = requests.get(get_url('quizinfo', self.id_))
        return response.json()
