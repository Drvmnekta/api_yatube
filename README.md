### Описание:

API для социальной сети YaTube.

Социальная сеть с возможностью регистрации и ведения своего блога.
Посты могут содержать изображения и текст. Также они могут быть объединены в сообщества.
Есть возможность подписаться на автора, прокомментировать пост, вступить в сообщество, читать общую ленту сайта или ленту своих подписок.

Позволяет делать запросы к моделям проекта: Посты, Группы, Комментарии, Подписки.
Поддерживает методы GET, POST, PUT, PATCH, DELETE
Предоставляет данные в формате JSON

### Технологии:
- Python 3.9
- Django REST Framework 3.12.4
- Django 2.2.16
- Djangorestframework-simplejwt 4.7.2
- Pillow 8.3.1


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Drvmnekta/api_yatube.git
```

```
cd api_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source venv/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Некоторые примеры запросов:

```
http://127.0.0.1:8000/api/v1/posts/
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}

```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```
{
  "text": "string"
}
