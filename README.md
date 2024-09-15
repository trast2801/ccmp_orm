# compare_orm
<p align="center">
**Сравнение ORM (Django, Tortoise, SqlAlchemy)  используя фреймворк Django**
  <br><br>
  <img src="https://i.ytimg.com/vi/2z58SHwQI6Y/maxresdefault.jpg">
</p>

## Цель проекта 
  Сравнение производительности и удобства использования различных ORM (Object-Relational Mapping) библиотек: Django ORM, SQLAlchemy и Tortoise ORM
  В качестве теста использовались стандартные для ORM CRUD функции

## Установка 

У вас должны быть установлены [зависимости проекта](https://github.com/trast2801/ccmp_orm/tree/master/Compare_Orm)

1. Клонирование репозитория 

```git clone https://github.com/trast2801/compare_orm```

2. Переход в директорию Compare_ORM

```cd Compare_ORM```

3. Создание виртуального окружения

```python3 -m venv venv```

4. Активация виртуального окружения

```source venv/bin/activate```

5. Установка зависимостей

```pip3 install -r requirements.txt```
6. Для Tortois нужно положить базу по пути (пока не нашел причину почему tortoise не видит относительный путь)
сама база находится в task1 её следует скопировать по пути приведнному ниже.  
```db_url="sqlite:///C:\\python_django2\\19module\\Compare_Orm\\db.sqlite3"```,

## Что применялось
<ul>
  <li>работа с файлами (импорт из csv в БД,  выгрузка/загрузка в текстовый файл)</li>
  <li>настройка   DJANGO для работы с Tortoise, SqlAlchemy (файл setting.py)</li>
  <li>создание трех типов моделей для каждой ORM (первая идея была сделать единый шаблон, но модели оказались не совместимы между собой)
  реализованы CRUD функции для каждой ORM</li>
  <li>Создание и использование HTML файлов для вывода результата. </li>
  <li>в первом ORM реализовано модели через классы и тесты также через методы классов, для оставшихся двух использовались функции.</li> 
</ul>

## Результат выполнения программы
  Были протестированы ОRM решения на базе Django ORM, SQLAlchemy,  Tortoise ORM , на различных наборах данных.  
Основные метрики, такие как скорость обработки запроса, время загрузки тестовых данных  были использованы для оценки производительности каждого решения. Для достижения целей проекта были созданы две таблицы, не связанные друг с другом средствами ORM. Но для проверки связывания средствами SQL, обладающие едиными полями (для связи один-ко-многим). БД содержит информацию о фильмах выпущенных в 20 веке. И вторая таблица собранные случайным образом рецензии на эти фильмы.

  Отображение результатов тестирования исполнено на базе HTML шаблона, расположенного в папке templates. В ходе выполнения вычислений заполняется словарь, который затем передается в указанный шаблон. 

![image](https://github.com/user-attachments/assets/fbd1b1b6-142c-4a0c-a200-2ac4221efc83)
  
