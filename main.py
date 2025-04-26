from database import *
from task import *
from datetime import datetime

db_path = "D:\Code\Projet_en_cours\Task Manager\data\data.db"

data = Data(db_path)
task_list = Task_list()

def get_task_from_list_sql(list_sql):
    return Task(list_sql[0],list_sql[1],list_sql[2],list_sql[3],list_sql[4],list_sql[5],list_sql[6])

for i in data.query("SELECT * FROM Task"):
    task_list.add_task_to_list(get_task_from_list_sql(i))

def dev_show_sync_data_list(): # Affiche les élément de la liste des tâches, en comparaison avec la base de donnée, pour vérifier leur synchronisation
    task_list.dev_show_task_list()
    data.dev_show_table("Task")



def add_task(id,name,detail="",created=datetime.now().strftime("%d/%m/%Y"),deadline=None,priority="normal",statut="running"): # !! Verifier l'id !!
    task_list.add_task_to_list(Task(id,name,detail,created,deadline,priority,statut))
    data.query(f"INSERT INTO Task VALUES ('{id}','{name}','{detail}','{created}','{deadline}','{priority}','{statut}')")
    
def remove_task(id):
    task_list.remove_task_to_list(id)
    data.query(f"DELETE FROM Task WHERE ID = {id}")





