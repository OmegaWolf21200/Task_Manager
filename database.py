import sqlite3 as sql
from tabulate import tabulate

db_path = "D:\Code\Projet_en_cours\Task Manager\data\data.db"

class Data:
    def __init__(self,path):
        self.path = path
        self.data = sql.connect(self.path)

    def query(self,query):
        cur = self.data.cursor()
        return list(cur.execute(query))
    
    def dev_show_table(self,table):
        tab = self.query(f"SELECT * FROM {table}")
        headers_raw = self.query(f"PRAGMA table_info({table})")
        header = list()
        for element in headers_raw:
            header.append(element[1])
        print(tabulate(tab,header,tablefmt="outline"))

    



data = Data(db_path)
data.dev_show_table("Task")