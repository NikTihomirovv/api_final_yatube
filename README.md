# api_final
### Описание проекта:
Это маленький учебный проект на тему API. В проекте созданы несколько моделей, сериализаторов и вьюсетов. Используются такие инструменты как Permissions, JWT-токены.
### Установка:
# 1) Клонировать репозиторий:
git clone https://github.com/NikTihomirovv/api_final_yatube
# 2) Развернуть виртуальное окружение и активировать его:
python -m virtualenv venv
python -m pip install --upgrade pip 
venv/scripts/activate 
# 3) Установить файл зависимостей:
python -m pip install -r requirements.txt
# 4) Выполнить миграции:
python manage.py migrate
# 5) Запустить проект:
python manage.py runserver

### Примеры запросов к API: 

# 1) Запрос на создание публикации:
http://127.0.0.1:8000/api/v1/posts/

Request Samples:
{
  "text": "string",
  "group": 0
}

Response Samples:
200
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}

401
{
  "detail": "Учетные данные не были предоставлены."
}

# 2) Запрос на получение комментария:
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/

Response Samples:
200
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}

404
{
  "detail": "Страница не найдена."
}

# 3) Запрос на получение JWT-токена:
http://127.0.0.1:8000/api/v1/jwt/create/

Request Samples:
{
  "username": "string",
  "password": "string"
}

Response Samples:
200
{
  "refresh": "string",
  "access": "string"
}

400
{
  "username": [
    "Обязательное поле."
  ],
  "password": [
    "Обязательное поле."
  ]
}




