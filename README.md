<div id="header" align="center">
  <img src="https://media.giphy.com/media/l41lRVmlnknDV3n9u/giphy.gif" width="100"/>
</div>

## <div align="center"> Api Yamdb </div>
API для проекта YaMDb, который собирает отзывы пользователей на произведения. Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Список категорий может быть расширен. Произведению может быть присвоен жанр из списка предустановленных. Пользователи могут оставить к произведениям текстовые отзывы и поставить произведению оценку, из пользовательских оценок формируется усреднённая оценка произведения — рейтинг.


## Технологии
![yamdb_workflow](https://github.com/maxxtor/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?branch=master&event=push)
![python version](https://img.shields.io/badge/Python-3.7-green)
![django version](https://img.shields.io/badge/Django-2.2-green)
![django rest framework version](https://img.shields.io/badge/Django%20REST%20Framework-3.2.14-green)
![docker version](https://img.shields.io/badge/Docker-20.10-green)
![docker-compose version](https://img.shields.io/badge/Docker--Compose-3.8-green)
![nginx version](https://img.shields.io/badge/Nginx-%201.18-green)


## Запуск приложения в контейнерах:
Для ОС на базе Linux. Клонировать репозиторий и перейти в папку с инфраструктурой в командной строке:

```
git clone https://github.com/mAXxtor/infra_sp2.git
```
```
cd infra_sp2/
```
```
cd infra/
```

Cоздать файл .env с переменными окружения, необходимыми для работы приложения:

```
touch .env
```
```
nano .env
```

Шаблон наполнения env-файла:

```
# Cекретный ключ Django проекта (https://djecrety.ir/)
SECRET_KEY=<ключ>

# Движок баз данных
DB_ENGINE=django.db.backends.postgresql

# Имя базы данных
DB_NAME=postgres

# Имя пользователя для базы данных:
POSTGRES_USER=<login>

# Пароль пользователя для базы данных:
POSTGRES_PASSWORD=<password>

# Название сервиса:
DB_HOST=db

# Порт для подключения к базе данных:
DB_PORT=5432
```

Развернуть контейнеры (в системе должен быть установлен и запущен Docker):

```
docker-compose up -d --build
```

Выполнить в контейнере web миграции:

```
docker-compose exec web python manage.py migrate
```

Создать суперпользователя:

```
docker-compose exec web python manage.py createsuperuser
```

Собрать статику в volume static_value:

```
docker-compose exec web python manage.py collectstatic --no-input
```

Проект доступен по адресу: [localhost](http://localhost/admin/)


## Загрузка тестовых значений в базу данных

Заполнить базу данных из тестовых файлов:

```
docker-compose exec web python manage.py load_test_data
```


## Примеры запросов к API:

Получение списка всех категорий:
```
GET
http://localhost/api/v1/categories/
```

Получение списка всех произведений:
```
GET
http://localhost/api/v1/titles/
```

Получение списка всех отзывов к произведению:
```
GET
http://localhost/api/v1/titles/{title_id}/reviews/
```

Получение списка всех комментариев к отзыву:
```
GET
http://localhost/api/v1/titles/{title_id}/reviews/{review_id}/comments/
```

### Полная документация по Api содержится в [ReDoc](http://localhost/redoc/).

### Авторы
[Yandex Practicum], [Максим Вербицкий]

[//]: #

   [Yandex Practicum]: <https://practicum.yandex.ru/>
   [Максим Вербицкий]: <https://github.com/mAXxtor>

