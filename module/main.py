# -*- coding: utf-8 -*-

import requests
email = "test@rmplatform.com"
password = "test1234"


class Login(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password

    login_dict = {"notify_method": "login", "email": email, "password": password}
    # Make login pass validation check

    def login_request(self):
        login_response = requests.post("http://rmnova.30meridian.com/API", json=self.login_dict)
        token = login_response.json()
        return token


class Fio(object):
    def __init__(self, filename):
        self.filename = filename

    def writing(self):
        print(Login().login_request())
        # with open(self.filename, "r+") as writed_file:
        #     writed_file.write(str(Login.login_request()))

    def parsing(self):
        with open(self.filename, "r+") as read_file:
            for line in read_file:
                token = line[11:43]
        return token


class LastNotify(object):
    def __init__(self, email, token): #Как передать token из Fio.parsing
        self.email = email
        self.token = token
        self.last_notify_params = {"notify_method": "get_last", "email": email, "token": token}

    def last_notify(self):
        get_last_notify_response = requests.post("http://rmnova.30meridian.com/API", json=self.last_notify_params)


testUser1 = Login(email, password)#передали мыло пароль в класс Login, сохранили в переменную
something = testUser1.login_request()#вызвали метод класса, сохранили в переменную
wr= Fio("config.xml").writing()#wr- переменная, хранящая вызов метода writing клaсса Fio (ЗАЧЕМ)
prs = Fio("config.xml").parsing()#переменная хранящая вызов метода parsing, который возвращает token
ln = LastNotify(email, prs)#object which saves email and token
ln.last_notify()#call last_notify method
