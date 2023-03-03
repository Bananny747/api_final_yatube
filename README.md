# api_final
api final

### Описание

Проект призван обепечить доступ к социальной сети Yatube посредством API. Хотя, если честно, он нужен для обучания автора.

### Примеры запросов к эндпоинтам

##### Получение списка публикаций / создание публикации
```
http://127.0.0.1:8000/api/v1/posts/
``` 
При создании публикации в теле запроса предлагается передать:
{
"text": "<Текст публикции>",
"image": "<Закодированное в виде текста с использованием стандарта Base64 изображение. Заполнение не обязательно.>",
"group": <id группы. Заполнение не обязательно.>
}

##### Получение/обновление/частичное обновление/удавление публикации
```
http://127.0.0.1:8000/api/v1/posts/{id}/
```

Полную докуметацию смотри тут: http://127.0.0.1:8000/redoc

### Технологии
Django 3.2.16
pytest 6.2.4
pytest-pythonpath 0.7.3
pytest-django 4.4.0
djangorestframework 3.12.4
djangorestframework-simplejwt 4.7.2
Pillow 9.3.0
PyJWT 2.1.0
requests 2.26.0
django-filter 2.4.0.


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Bananny747/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
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