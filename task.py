from datetime import datetime
from tabulate import tabulate
from database import *

headers = ["id","name","detail","created","deadline","priority","statut"]

class Task:

    def __init__(self,id,name,detail,created=datetime.now().strftime("%d/%m/%Y"),deadline=None,priority="normal",statut="running"):
        self.id = id
        self.name = name
        self.detail = detail
        self.deadline = deadline
        self.created = created
        self.priority = priority
        self.statut = statut


    def get_task(self):
        return [self.id,self.name,self.detail,self.created,self.deadline,self.priority,self.statut]
    
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def show_task(self):
        print(tabulate([self.get_task()],headers,tablefmt="outline"))


class Task_list:

    def __init__(self):
        self.tasks = list()

    def add_task(self,task: Task):
        self.tasks.append(task)

    def show_task_list(self):
        tab = list()
        for task in self.tasks:
            tab.append(task.get_task())
        print(tabulate(tab,headers,tablefmt="outline"))

    def remove_task(self,id):
        for task in self.tasks:
            if task.get_id() == id:
                self.tasks.remove(task)