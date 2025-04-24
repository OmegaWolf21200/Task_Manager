from datetime import datetime
from tabulate import tabulate
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
        headers = ["id","name","detail","created","deadline","priority","statut"]
        print(tabulate([self.get_task()],headers,tablefmt="outline"))

    
    

