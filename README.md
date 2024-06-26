# grade_book


# Предварительные требования
Для запуска проекта на Windows или Linux вам понадобятся:

- Python 3.8+
- Git
- Виртуальное окружение (рекомендуется)


## Клонирование репозитория

Сначала нужно клонировать репозиторий проекта. Откройте терминал или командную строку и выполните следующую команду:

    git clone https://github.com/almas-rak/grade_book.git

Перейти в папку репозитория

    cd grade_book

## Установка зависимостей
    
### Windows:
    
Создайте виртуальное окружение:

    python -m venv venv

Активируйте его:

    venv\Scripts\activate

Установите зависимости:

    pip install -r requirements.txt

### Linux:

Создайте виртуальное окружение:

    python3 -m venv venv

Активируйте его:

    source venv/bin/activate

Установите зависимости:

    pip install -r requirements.txt

## Настройка базы данных

Проект использует SQLite. Для создания базы данных и применения миграций выполните следующие команды

Перейдите в папку source

    cd source

Сгенерируйте первую миграцию:

    alembic revision --autogenerate -m "Initial migration"


Примените миграции: 

    alembic upgrade head

## Запуск приложения

Запустите приложение FastAPI с помощью Uvicorn:

    uvicorn main:app 

Приложение будет доступно по адресу http://127.0.0.1:8000.

## Документация API

Документация API доступна по следующим URL:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

