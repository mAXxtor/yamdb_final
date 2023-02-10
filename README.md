<div id="header" align="center">
  <img src="https://media.giphy.com/media/l41lRVmlnknDV3n9u/giphy.gif" width="100"/>
</div>

# <div align="center"> CI/CD для проекта Api Yamdb </div>
CI/CD для проекта API YaMDb, который собирает отзывы пользователей на произведения. Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Список категорий может быть расширен. Произведению может быть присвоен жанр из списка предустановленных. Пользователи могут оставить к произведениям текстовые отзывы и поставить произведению оценку, из пользовательских оценок формируется усреднённая оценка произведения — рейтинг.

Временно доступен по адресу [проект](http://tubemax.hopto.org/admin/)
Для ревьюера создана учетка test/test


## Технологии
[![yamdb_workflow](https://github.com/maxxtor/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?branch=master&event=push)](https://github.com/maxxtor/yamdb_final/actions/workflows/yamdb_workflow.yml)
[![python version](https://img.shields.io/badge/Python-3.7-green)](https://www.python.org/)
[![django version](https://img.shields.io/badge/Django-2.2-green)](https://www.djangoproject.com/)
![django rest framework version](https://img.shields.io/badge/Django%20REST%20Framework-3.2.14-green)
[![PostgreSQL](https://img.shields.io/badge/PostgresSQL-13.0-green)](https://www.postgresql.org/)
[![docker version](https://img.shields.io/badge/Docker-20.10-green)](https://www.docker.com/)
[![docker-compose version](https://img.shields.io/badge/Docker--Compose-3.8-green)](https://www.docker.com/)
[![nginx version](https://img.shields.io/badge/Nginx-%201.18-green)](https://nginx.org/ru/)
[![docker hub](https://img.shields.io/badge/-Docker%20Hub-464646?style=flat&logo=Docker&logoColor=56C0C0&color=515151)](https://www.docker.com/products/docker-hub)
[![github%20actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat&logo=GitHub%20actions&logoColor=56C0C0&color=515151)](https://github.com/features/actions)
[![yandex.cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat&logo=Yandex.Cloud&logoColor=56C0C0&color=515151)](https://cloud.yandex.ru/)


## Workflow:
* tests - Проверка кода на соответствие стандарту PEP8 (с помощью пакета flake8) и запуск pytest. Дальнейшие шаги выполнятся только если push был в ветку master или main.
* build_and_push_to_docker_hub - Сборка и доставка docker-образа для контейнера на Docker Hub
* deploy - Автоматический деплой проекта на удаленный сервер.
* send_message - Отправка уведомления о статусе workflow в Telegram через бота


## Подготовка сервера:
Войти на свой удаленный сервер, установить и запустить [Docker](https://docs.docker.com/engine/install/) и [Docker-compose](https://docs.docker.com/compose/install/):
```
sudo apt install docker.io
sudo apt install docker-compose
sudo systemctl start docker
```
Для работы ssl сертификата установить certbot, поочередно выполнив команды:
```
sudo apt install snapd
sudo snap install core; sudo snap refresh core
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
```
Скачать скрипт в рабочую директорию:
```
curl -L https://raw.githubusercontent.com/wmnnd/nginx-certbot/master/init-letsencrypt.sh > init-letsencrypt.sh
```
Отредактировать скрипт. Добавить домен в переменную domains и действующую электронную почту в переменную email:
```
nano init-letsencrypt.sh
```
Добавляем разрешения на запуск скрипта и запускаем его:
```
chmod +x init-letsencrypt.sh
sudo ./init-letsencrypt.sh
```


## Настройка и запуск приложения в контейнерах:
Сделать fork репозитория, клонировать и перейти в папку с инфраструктурой в командной строке:
```
git clone https://github.com/<username>/yamdb_final.git
```
```
cd yamdb_final/infra/
```
Скопировать файлы docker-compose.yaml и nginx/default.conf из проекта на сервер:
```
scp ./docker-compose.yaml <username>@<host>:/home/<username>/
scp ./nginx/default.conf <username>@<host>:/home/<username>/nginx/
```
Добавить в [Secrets GitHub Actions](https://github.com/<username>/yamdb_final/settings/secrets/actions) переменные окружения для работы базы данных, приложения и workflow:
```
# Cекретный ключ Django проекта (https://djecrety.ir/)
SECRET_KEY=<ключ>

# Разрешенные хосты/домены для которых работает Django проект (открыть доступ для всех - '*')
ALLOWED_HOSTS=<'*'>

# Движок базы данных
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

# Логин на Docker Hub:
DOCKER_USERNAME=<login>

# Пароль на Docker Hub:
DOCKER_PASSWORD=<password>

# IP-адрес удаленного сервера:
HOST=<IP>

# Логин на удаленном сервере:
USER=<login>

# Пароль на удаленном сервере:
PASSPHRASE=<password>

# Приватный ssh-ключ (публичный должен быть на сервере):
SSH_KEY=<key>

# ID своего telegram аккаунта (https://t.me/userinfobot):
TELEGRAM_TO=<id> 

# Token telegram бота (https://t.me/BotFather):
TELEGRAM_TOKEN - токен бота (получить токен можно у @BotFather, /token, имя бота)
```
Для использования тестовой базы данных SQLlite добавить в [Variables GitHub Actions](https://github.com/<username>/yamdb_final/settings/variables/actions):
```
# Булево значение для подключения базы данных SQLlite (True) вместо PostgreSQL (False):
TEST_DB=<True/False>
```
Развернуть контейнеры через терминал на удаленном сервере:
```
sudo docker-compose up -d --build
```

Выполнить в контейнере web миграции:
```
sudo docker-compose exec web python manage.py migrate
```

Создать суперпользователя:
```
sudo docker-compose exec web python manage.py createsuperuser
```

Собрать статику в volume static_value:
```
sudo docker-compose exec web python manage.py collectstatic --no-input
```


## Загрузка тестовых значений в базу данных

При необходимости, заполнить базу данных из тестовых файлов:
```
sudo docker-compose exec web python manage.py load_test_data
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
