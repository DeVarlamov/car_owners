# ЯмыАвто
Социальная сеть для любитей автомобилей с интеграциией новостей

### Возможности проекта 
- Пользователям  могут выполнять CRUD операции
	(Создание, Чтение, Обновление, Удаление) с записями в базе данных.
	Подписываться друг на друга, добовлять посты, редактировать посты, удалять посты.

- Ананимные и зарегестрированные пользователи могут смотреть новости

### **ЗАМЕЧАНИЕ**:
* Для запуска проекта потребуется два теримнала, запуск фоновых задач и запуск основного приложения

Стек:

- aiohttp==3.9.1
- aiosignal==1.3.1
- asgiref==3.2.10
- atomicwrites==1.4.1
- attrs==23.1.0
- certifi==2023.11.17
- chardet==3.0.4
- Django==3.1
- django-background-tasks==1.2.5
- django-compat==1.0.15
- django-debug-toolbar==2.2
- Faker==12.0.1
- frozenlist==1.4.0
- funcy==2.0
- idna==2.8
- mixer==7.1.2
- more-itertools==10.1.0
- multidict==6.0.4
- packaging==23.2
- Pillow==9.4.0
- pluggy==0.13.1
- psycopg2==2.9.9
- py==1.11.0
- python-dateutil==2.8.2
- python-dotenv==1.0.0
- pytz==2023.3.post1
- redis==5.0.1
- requests==2.22.0
- six==1.14.0
- sorl-thumbnail==12.6.3
- sqlparse==0.4.4
- tzdata==2023.3
- urllib3==1.25.11
- wcwidth==0.2.12
- yarl==1.9.3

### Настройка и запуск на ПК

Клонируем проект:

```bash
git clone git@github.com:DeVarlamov/car_owners.git
```

Устанавливаем виртуальное окружение:

```bash
python -m venv venv
```

Активируем виртуальное окружение:

```bash
source venv/Scripts/activate
```

> Для деактивации виртуального окружения выполним (после работы):
> ```bash
> deactivate
> ```

Устанавливаем зависимости:

```bash
python -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

Применяем миграции:

```bash
python mycar/manage.py makemigrations
python mycar/manage.py migrate
```

Создаем супер пользователя:

```bash
python mycar/manage.py createsuperuser
```

В папку с проектом, где файл settings.py добавляем файл .env куда прописываем наши параметры:

```bash
SECRET_KEY='Ваш секретный ключ'
ALLOWED_HOSTS='127.0.0.1, localhost'
DEBUG=True

POSTGRES_USER='Пользователь'
POSTGRES_PASSWORD='Пароль пользователя'
POSTGRES_DB='Название ДБ'
DB_HOST='Хост ДБ'
DB_PORT='Порт ДБ'

USE_DB = 'True'(SQLlite) или 'False'(Posgress) в зависимости от какую

API_KEY = 'Ваш токен от ресурса новостей с сайта ' https://newsapi.org/
```

Не забываем добавить в .gitingore файлы:

```bash
.env
.venv
```

Для запуска тестов выполним:

```bash
python mycar/manage.py test
```

Получим:

```bash
$ python manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
...............................
----------------------------------------------------------------------
Ran 31 tests in 4.986s

OK
Destroying test database for alias 'default'...
```

Запускаем проект: в первом терминале

```bash
python mycar/manage.py runserver localhost:80
```
Запускаем во втором терминале фоновые задачи
```bash
python mycar/manage.py process_tasks
```


После чего проект будет доступен по адресу http://localhost/

Заходим в http://localhost/admin и создаем группы и записи.
После чего записи и группы появятся на главной странице.

Автор: [Варламов Николай](https://github.com/devarlamov) :+1:
