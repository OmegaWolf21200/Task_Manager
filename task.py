from datetime import datetime
from tabulate import tabulate

headers = ["id","name","detail","created","deadline","priority","statut"] #Liste des headers pour l'affichage des tableau

class Task:

    def __init__(self,id,name,detail,created,deadline,priority,statut):
        self.id = id
        self.name = name
        self.detail = detail
        self.deadline = deadline
        self.created = created
        self.priority = priority
        self.statut = statut


    def get_task(self): # Retourne toutes les propriétés de la tâche
        return [self.id,self.name,self.detail,self.created,self.deadline,self.priority,self.statut]
    
    def get_id(self): # Retourne l'id de la tâche
        return self.id
    
    def get_name(self): # Retourne le nom de la tâche
        return self.name
    
    def dev_show_task(self): # Affiche un tableau des propriété de la tâches
        print(tabulate([self.get_task()],headers,tablefmt="outline"))


class Task_list:

    def __init__(self):
        self.tasks = list()

    def get_raw_task_list(self):
        return self.tasks

    def dev_show_task_list(self): #Affiche un tableau de l'ensemble des tâches dans la liste
        tab = list()
        for task in self.tasks:
            tab.append(task.get_task())
        print(tabulate(tab,headers,tablefmt="outline"))

    def add_task_to_list(self,task: Task):
        self.tasks.append(task)

    def remove_task_to_list(self,id):
        for task in self.tasks:
            if task.get_id() == id:
                self.tasks.remove(task)