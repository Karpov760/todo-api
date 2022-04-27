import requests
import json
import tkinter as tk
import tkinter.messagebox as mb
from pprint import pprint

class Api_connect:

    def __init__(self):
        self.url_str = 'http://localhost:5000/todo/api/tasks'

    def get_tasks(self):
        response = requests.get(self.url_str)
        return response.text

    def get_task(self, id):
        response = requests.get(f"{self.url_str}/{id}")
        return response.text

    def del_task(self, id):
        response = requests.delete(f"{self.url_str}/{id}")
        answer = ''
        if response.status_code == 200:
            answer = "Задача удалена"
        return answer

    def post_task(self, title, description):
        param = {"title": title, 'description': description}
        response = requests.post(
            self.url_str,
            json=param
        )
        answer = ''
        if response.status_code == 201:
            answer = "Задача внесена в список"
        return answer



if __name__ == "__main__":
    ac = Api_connect()
    while(True):
        print("Выберите действие: ")
        print("1. Посмотреть список задач ")
        print("2. Посмотреть задачу: ")
        print("3. Добавить задачу ")
        print("4. Удалить задачу ")

        x = int(input())
        if (x == 1):
            pprint(ac.get_tasks())

        if (x == 2):
            id = int(input("Номер задачи: "))
            pprint(ac.get_task(id))

        if (x == 3):
            title = input("Заголовок:")
            des = input("Описание:")
            pprint(ac.post_task(title, des))

        if (x == 4):
            id = int(input("Номер задачи: "))
            pprint(ac.del_task(id))


