from database import *
from task import *
from datetime import datetime

db_path = "D:\Code\Projet_en_cours\Task Manager\data\data.db"

data = Data(db_path)
task_list = Task_list()

#Chargement des données
def get_task_from_list_sql(list_sql):
    return Task(list_sql[0],list_sql[1],list_sql[2],list_sql[3],list_sql[4],list_sql[5],list_sql[6])

for i in data.query("SELECT * FROM Task"):
    task_list.add_task_to_list(get_task_from_list_sql(i))


def dev_show_sync_data_list(): # Affiche les élément de la liste des tâches, en comparaison avec la base de donnée, pour vérifier leur synchronisation
    task_list.dev_show_task_list()
    data.dev_show_table("Task")


def add_task(id,name,detail="",created=datetime.now().strftime("%d/%m/%Y"),deadline="",priority="normal",statut="running"): # !! Verifier l'id !!
    task_list.add_task_to_list(Task(id,name,detail,created,deadline,priority,statut))
    data.query(f"INSERT INTO Task VALUES ({id},\"{name}\",\"{detail}\",\"{created}=\",\"{deadline}\",\"{priority}\",\"{statut}\")")
    
def remove_task(id_task):
    task_list.remove_task_to_list(id_task)
    data.query(f"DELETE FROM Task WHERE ID = {id_task}")

def edit_task(id_task,n_id=None,n_name=None,n_detail=None,n_created=None,n_deadline=None,n_priority=None,n_statut=None):
    task_list.edit_task_to_list(id_task,n_id,n_name,n_detail,n_created,n_deadline,n_priority,n_statut)
    temp_task = task_list.get_task_to_list(id_task if n_id == None else n_id) #Prendre l'id d'origine si l'id n'a pas été modifié, sinon prendre le nouvel id
    #Mettre a jour la table
    data.query(f"UPDATE Task SET {headers[0]} = {temp_task.get_id()},{headers[1]} = \"{temp_task.get_name()}\",{headers[2]} = \"{temp_task.get_detail()}\",{headers[3]} = \"{temp_task.get_created()}\",{headers[4]} = \"{temp_task.get_deadline()}\",{headers[5]} = \"{temp_task.get_priority()}\",{headers[6]} = \"{temp_task.get_statut()}\" WHERE ID = {id_task}")

