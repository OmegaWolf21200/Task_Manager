from datetime import datetime
from tabulate import tabulate

headers = ["ID","Name","Detail","Created","Deadline","Priority","Statut"] #Liste des headers pour l'affichage des tableau

class Task:

    def __init__(self,id,name,detail,created,deadline,priority,statut):
        self.id = id
        self.name = name
        self.detail = detail
        self.deadline = deadline
        self.created = created
        self.priority = priority
        self.statut = statut

    #GET

    def get_task(self): # Retourne toutes les propriétés de la tâche
        return [self.id,self.name,self.detail,self.created,self.deadline,self.priority,self.statut]
    
    def get_id(self): # Retourne l'id de la tâche
        return self.id
    
    def get_name(self): # Retourne le nom de la tâche
        return self.name
    
    def get_detail(self):
        return self.detail
    
    def get_created(self):
        return self.created
    
    def get_deadline(self):
        return self.deadline
    
    def get_priority(self):
        return self.priority
    
    def get_statut(self):
        return self.statut

    #SET

    def set_id(self,n_id):
        self.id = n_id

    def set_name(self,n_name):
        self.name = n_name

    def set_detail(self,n_detail):
        self.detail = n_detail

    def set_created(self,n_created):
        self.created = n_created

    def set_deadline(self,n_deadline):
        self.deadline = n_deadline

    def set_priority(self,n_priority):
        self.priority = n_priority

    def set_statut(self,n_statut):
        self.statut = n_statut

    def set_task(self,n_id=None,n_name=None,n_detail=None,n_created=None,n_deadline=None,n_priority=None,n_statut=None):
        def do_modification(func,var):
            func(var) if var != None else None

        do_modification(self.set_id,n_id)
        do_modification(self.set_name,n_name)
        do_modification(self.set_detail,n_detail)
        do_modification(self.set_created,n_created)
        do_modification(self.set_deadline,n_deadline)
        do_modification(self.set_priority,n_priority)
        do_modification(self.set_statut,n_statut)
        
        

    #Méthode

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

    def get_task_to_list(self,id_task):
        for task in self.tasks:
            if task.get_id() == id_task:
                return task
        

    def add_task_to_list(self,task: Task):
        self.tasks.append(task)

    def remove_task_to_list(self,id):
        for task in self.tasks:
            if task.get_id() == id:
                self.tasks.remove(task)

    def edit_task_to_list(self,id_task,n_id=None,n_name=None,n_detail=None,n_created=None,n_deadline=None,n_priority=None,n_statut=None):
        for task in self.tasks:
            if task.get_id() == id_task:
                task.set_task(n_id,n_name,n_detail,n_created,n_deadline,n_priority,n_statut)
            
