import sqlite3 as sql
from tabulate import tabulate

class Data:
    def __init__(self,path): #Init de la connexion avec la base de donnée
        self.path = path
        self.data = sql.connect(self.path)

    def query(self,query): #Retourne le resultat d'une requete SQL
        cur = self.data.cursor()
        return list(cur.execute(query))
    
    def dev_show_table(self,table): #Renvoie le contenue d'une table SQL dans la console de manière lisible
        tab = self.query(f"SELECT * FROM {table}") #Récupère tout le contenue de la table
        headers_raw = self.query(f"PRAGMA table_info({table})") #Récupère le nom et propriété de toute les colonne de la table
        header = list()
        for element in headers_raw: #Récupère uniquement le nom des colonnes des propriété des colonne de la table
            header.append(element[1])
        print(tabulate(tab,header,tablefmt="outline"))