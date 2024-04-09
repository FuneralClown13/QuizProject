SOCKET = '127.0.0.1:4000'


def add_id(endpoint):
    """
    замыкает кндпоинт для дальнейшего добавления id,
    если id необходим для api запроса
    """
    def wrapper(id_=None):
        if id_:
            return f'{endpoint}{id_}/'
        return endpoint
    return wrapper


api_endpoints = {
    'quiz': add_id('api/v1/quiz/'),
    'question': add_id('api/v1/question/'),
    'quizquestions': add_id('api/v1/quizquestions/'),
    'quizinfo': add_id('api/v1/quizinfo/'),

}


def get_url(key, id_=None):
    """
    Возвращает собраный url
    :param key: ключ для словаря api_endpoints
    :param id_: id quiz или question
    :return: url
    """
    if key in api_endpoints:
        return f'http://{SOCKET}/{api_endpoints[key](id_)}'
