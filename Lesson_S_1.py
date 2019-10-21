# Урок 1. Основы клиент-серверного взаимодействия. Парсинг API

# 1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя,
# сохранить JSON-вывод в файле *.json.

# 2. Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа). Выполнить запросы к нему, пройдя авторизацию через curl, Postman, Python.Ответ сервера записать в файл (приложить скриншот для Postman и curl).

# 3. Кто плохо знаком с html/css изучаем курс: https://geekbrains.ru/courses/108 Для html/css вам нужны 3,4,5 уроки

# Инструкция к сдаче

# Настоятельно рекомендуем сдавать практическое задание в виде ссылки на pull request.

# Рекомендуемый способ организации данных в репозитории: создать отдельные папки по темам и помещать в них отдельные файлы для каждой задачи с правильным расширением.

# Ссылка на инструкцию по работе с git и сдачу практики:

# https://docs.google.com/document/d/1RAT_ukE39iOfbz1xa39QXae2hBUEZ4U6Fko_wFDdrsM/edit
# Ссылка на видеокурс по Git:

# https://geekbrains.ru/courses/66
# Если остались сложности с системой git, обратитесь к преподавателю или наставнику.

import json
import requests

# 1

url = "https://api.github.com/users/Mikhail2018/repos"
data = requests.get(url)
print(data)

jdata = data.json()
result_data = []
result_data.extend(jdata)

with open ('github_repos.json', 'w') as jfile:
    jfile.write(json.dumps(result_data))