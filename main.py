from database import *
from task import *

db_path = "D:\Code\Projet_en_cours\Task Manager\data\data.db"

data = Data(db_path)
task_list = Task_list()

def get_task_from_list_sql(list_sql):
    return Task(list_sql[0],list_sql[1],list_sql[2],list_sql[3],list_sql[4],list_sql[5],list_sql[6])


for i in data.query("SELECT * FROM Task"):
    task_list.add_task(get_task_from_list_sql(i))



