#### Проект Yatube_API, служит для доступа через программный интерфейс к возможностям Yatube, таким как:
- получение постов/поста, его создание, редактирование, удаление;
- получение комментариев/комментария, его создание, редактирование, удаление;
- получение групп;
- получение подписки и подписка на интересующего автора.
Кроме того в данном проекте реализован доступ через JWT-token. 
Что позволяет контролировать использование пользователями контента, через ограничение их прав.

#### Как развернуть проект и запустить его на локальной машине:

**Клонировать репозиторий и перейти в него в командной строке:**
```
git clone [https://github.com/RomanBaykin/api_final_yatube.git]
cd api_final_yatube
```
**Cоздать и активировать виртуальное окружение:****
```
Linux/Mac OS:
python3 -m venv env
source env/bin/activate
Windows:
python -m venv env
env/scripts/activate
```
**Установить зависимости из файла requirements.txt:**
```
Linux/Mac OS:
python3 -m pip install --upgrade pip
pip install -r requirements.txt
Windows:
python -m pip install --upgrade pip
pip install -r requirements.txt
```
**Выполнить миграции:**
```
Linux/Mac OS:
python3 manage.py migrate
Windows:
python manage.py migrate
```
**Запустить проект:**
```
Linux/Mac OS:
python3 manage.py runserver
Windows:
python manage.py runserver
```
#### Примеры доступных эндпоинтов:
- получение JWT-токена: [http://127.0.0.1:8000/api/v1/jwt/create/(указываются username и password)]
- получение постов: [http://127.0.0.1:8000/api/v1/posts/?limit=5&offset=1] (limit - количество постов на странице, offset - с какого поста начинается отсчёт)
- создание поста: [http://127.0.0.1:8000/api/v1/posts/(указываются text и group)]
