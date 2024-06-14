[![Linter check](https://github.com/ReYaNOW/mediasoft-test-task/actions/workflows/pyci.yml/badge.svg)](https://github.com/ReYaNOW/mediasoft-test-task/actions/workflows/pyci.yml)  


## Описание
Тестовое задание для MediaSoft

REST API, созданное при помощи DRF для работы с сущностями city, street, shop.  
  
Реализована возможность поднятия БД в Docker.  
Реализована валидация входных данных.

Стек: Python3.11, DRF, psycopg2, Docker

## Документация
Открыть документацию можно по [ссылке](https://mediasoft-test-task.onrender.com/docs)  
Там же можно поделать запросы к сервису

# Использование


 - Открыть задеплоенный на [тестовый вариант](https://mediasoft-test-task.onrender.com)
 - [Развернуть сервис локально](#Как-развернуть-сервис-локально)

![App preview](https://github.com/ReYaNOW/ReYaNOW/blob/main/Images/mediasoft_preview.png?raw=true)

## Как развернуть сервис локально
Для этого необходим [Poetry](https://python-poetry.org/docs/#installing-with-pipx)  
  
1. Склонировать репозиторий  

```
git clone https://github.com/ReYaNOW/mediasoft-test-task.git
```

2. Переименовать .env.example в .env  
  
```
mv .env.example .env
```

3. Поднять PostgreSQL через Docker или указать другую database url в .env для использования своей БД.  
   В ином случае DRF будет использовать SQLite.

```
make start-db
```

4. Установить зависимости, применить миграции к БД, создать аккаунт для админки  
   Username: admin, password: admin
  
```
make install
```

5. Запустить локальный сервер и открыть http://127.0.0.1:8080
  
```
make start
```
