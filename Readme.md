## Задача №1

имеется текстовый файл file.csv, в котром разделитель полей с данными: | (верт. черта)
пример ниже содержит небольшую часть этого файла(начальные 3 строки, включая строку заголовков полей)
"""
lastname|name|patronymic|date_of_birth|id
Фамилия1|Имя1|Отчество1 |21.11.1998 |312040348-3048
Фамилия2|Имя2|Отчество2 |11.01.1972 |457865234-3431
...
"""
Задание
1. Реализовать сбор уникальных записей
2. Случается, что под одиннаковым id присутствуют разные данные - собрать отдельно такие записи

## Задача №2

в наличии список множеств. внутри множества целые числа
m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]
Задание: посчитать
1. общее количество чисел
2. общую сумму чисел
3. посчитать среднее значение
4. собрать все множества в один кортеж
*написать решения в одну строку

## Задача №3

имеется список списков
a = [[1,2,3], [4,5,6]]
Задание:
сделать список словарей
b = [{'k1': 1, 'k2': 2, 'k3': 3}, {'k1': 4, 'k2': 5, 'k3': 6}]
*написать решение в одну строку

## Задача №4

Имеется папка с файлами
Реализовать удаление файлов старше N дней

## Задача №5

В наличии текстовый файл с набором русских слов(имена существительные, им.падеж)
Одна строка файла содержит одно слово.
Задание:
Написать программу которая выводит список слов,
каждый элемент списка которого - это новое слово,
которое состоит из двух сцепленных в одно, которые имеются в текстовом файле.
Порядок вывода слов НЕ имеет значения
Например, текстовый файл содержит слова:
ласты
стык
стыковка
баласт
кабала
карась

Пользователь вводмт первое слово: ласты
Программа выводит:
ластык
ластыковка
Пользователь вводит первое слово: кабала
Программа выводит:
кабаласты
кабаласт
Пользователь вводит первое слово: стыковка
Программа выводит:
стыковкабала
стыковкарась

## Задача №6

Имеется банковское API возвращающее JSON
{
"Columns": ["key1", "key2", "key3"],
"Description": "Банковское API каких-то важных документов",
"RowCount": 2,
"Rows": [
["value1", "value2", "value3"],
["value4", "value5", "value6"]
]
}
Основной интерес представляют значения полей "Columns" и "Rows",
которые соответственно являются списком названий столбцов и значениями столбцов
Задание:
1. Получить JSON из внешнего API
ендпоинт: GET https://api.gazprombank.ru/very/important/docs?documents_date={"начало дня
сегодня в виде таймстемп"}
2. Валидировать входящий JSON используя модель pydantic
(из ТЗ известно что поле "key1" имеет тип int, "key2"(datetime), "key3"(str))
3. Представить данные "Columns" и "Rows" в виде плоского csv-подобного pandas.DataFrame
4. В полученном DataFrame произвести переименование полей по след. маппингу
"key1" -> "document_id", "key2" -> "document_dt", "key3" -> "document_name"
5. Полученный DataFrame обогатить доп. столбцом:
"load_dt" -> значение "сейчас"(датавремя)