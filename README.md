# Cервис Foodgram, "Продуктовый помощник"

## Описание

Онлайн-сервис Foodgram и API для него.Имеется реализация CI/CD проекта.На этом сервисе пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список "Избранное", а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

### Доступный функционал

- У неаутентифицированных пользователей доступ к API только на уровне чтения.
- Создание объектов разрешено только аутентифицированным пользователям.На прочий фунционал наложено ограничение в виде административных ролей и авторства.
- Управление пользователями.
- Возможность получения подробной информации о себе и ее редактирование.
- Возможность подписаться на других пользователей и отписаться от них.
- Получение списка всех тегов и ингредиентов.
- Получение списка всех рецептов, их добавление.Получение, обновление и удаление конкретного рецепта.
- Возможность добавить рецепт в избранное.
- Возможность добавить рецепт в список покупок.
- Возможность скачать список покупок в PDF формате.
- Фильтрация по полям.


#### Технологи

- Python 3.9
- Django 3.2.15
- Django Rest Framework 3.12.4
- Authtoken
- Docker
- Docker-compose
- PostgreSQL
- Gunicorn
- Nginx
- GitHub Actions

#### Локальный запуск проекта

- Склонировать репозиторий:

```bash
   git clone git@github.com:Alexstom007/foodgram-project-react.git
```

```bash
   cd foodgram-project-react
```

Cоздать и активировать виртуальное окружение:

Команда для установки виртуального окружения на Mac или Linux:

```bash
   python3 -m venv env
   source env/bin/activate
```

Команда для Windows:

```bash
   python -m venv venv
   source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```bash
   cd ..
   cd backend
   pip install -r requirements.txt
```

```bash
   python manage.py migrate
```

Заполнить базу тестовыми данными об ингредиентах и тегах:

```bash
   python manage.py load_ingredients
   python manage.py add_tags
```

Создать суперпользователя, если необходимо:

```bash
python manage.py createsuperuser
```

- Запустить локальный сервер:

```bash
   python manage.py runserver
```

#### Установка на удалённом сервере

- Выполнить вход на удаленный сервер
- Установить docker:

```bash
   sudo apt install docker.io
   ```

- Установить docker-compose:

``` bash
    sudo apt install docker-compose     
```


- Находясь локально в директории infra/, скопировать файлы docker-compose.production.yml и nginx.conf на удаленный сервер:

```bash
scp docker-compose.production.yml <username>@<host>:/home/<username>/
scp nginx.conf <username>@<host>:/home/<username>/
```

- Для правильной работы workflow необходимо добавить в Secrets данного репозитория на GitHub переменные окружения:

```bash
Переменные PostgreSQL, ключ проекта Django и их значения по-умолчанию можно взять из файла .env, затем установить свои.

DOCKER_USERNAME=<имя пользователя DockerHub>
DOCKER_PASSWORD=<пароль от DockerHub>

USER=<username для подключения к удаленному серверу>
HOST=<ip сервера>
PASSPHRASE=<пароль для сервера, если он установлен>
SSH_KEY=<ваш приватный SSH-ключ (для получения команда: cat ~/.ssh/id_rsa)>

TELEGRAM_TO=<id вашего Телеграм-аккаунта>
TELEGRAM_TOKEN=<токен вашего бота>
```

#### Зайдите на боевой сервер

- Примените миграции:

```bash
   sudo docker-compose.production.yml exec backend python manage.py migrate
```

- Создайте суперпользователя:

```bash
   sudo docker-compose.production.yml exec backend python manage.py createsuperuser
```

#### Примеры некоторых запросов API

Регистрация пользователя:

```bash
   POST /api/users/
```

Получение данных своей учетной записи:

```bash
   GET /api/users/me/ 
```

Добавление подписки:

```bash
   POST /api/users/id/subscribe/
```

Обновление рецепта:
  
```bash
   PATCH /api/recipes/id/
```

Удаление рецепта из избранного:

```bash
   DELETE /api/recipes/id/favorite/
```

Получение списка ингредиентов:

```bash
   GET /api/ingredients/
```

Проект доступен по адресу: <http://foodgram007.zapto.org>

Доступ в админку:

```bash
   email - asd@asd.ru
   пароль - 1234
```

#### Автор

Александр Вотинов- [https://github.com/Alexstom007](https://github.com/Alexstom007)