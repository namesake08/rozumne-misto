import requests
#from time import sleep

e = input("Введите email: ")
p = input("Введите password: ")

login_dict = {
    "notify_method": "login",
    "email": "",
    "password": "",
}

"""Заполнение login_dict словаря вручную"""
login_dict["email"] = "test@rmplatform.com"
login_dict["password"] = "test1234"
print(login_dict)

"""Выполнение login запроса на основе login_словаря"""
login_resp = requests.post("http://rmnova.30meridian.com/API", json=login_dict)
token = login_resp.json()

"""Открыли- записали токен -закрыли файл"""
f1 = open("config.xml", "r+")
f1.write(str(token) + "\n")
f1.close()

"""Выделение 32-х символьного токена из файла"""
f2 = open("config.xml", "r")
for line in f2.readlines():
    print(line[0:11] + "/n")
    print(line[12:43])
    token = line[11:43]
    print(token)
f2.close()

"""Создание словаря для get_last запроса"""
get_last_dict = {
    "notify_method": "get_last",
    "email": "",
    "token": "",
}

"""Заполнение get_last_dict словаря вручную"""
get_last_dict["email"] = "test@rmplatform.com"
get_last_dict["token"] = str(token)
print(get_last_dict)

"""Выполнение запроса получения последней нотификации"""
# json = {"notify_method": "get_last", "email": "test@rmplatform.com", "token": "0bd47f62285547cd9f3ca8e138b6e7e3"})
get_last_resp = requests.post("http://rmnova.30meridian.com/API", json=get_last_dict)
# {"notifies": []} - ответ при отсутствующих нотификациях
# {"notifies": [{"activity": "notify_description", "datetime": "2017-02-20T17:14:14.137227+00:00", "title": "notify_name",
#  "url": "http://rmnova.30meridian.com/admin/system/notify/add/"}]} - пример ответа при заполненной нотификации
print(get_last_resp.json())
