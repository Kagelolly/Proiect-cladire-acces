
import sqlite3
from constants import DB_NAME

class AccessDatabase:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.cursor = self.conn.cursor()

# Creare tabel Access pentru angajazti : 
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Access (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Id_Person INTEGER,
                Date TIMESTAMP,
                Direction VARCHAR(3),
                Gate INTEGER
            )
        ''')

 # Creare tabel Persoane :
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Persons (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Name VARCHAR(50),
                Surname VARCHAR(50),
                Company VARCHAR(50),
                Id_Manager INTEGER,
                Email VARCHAR(50)
            )
        ''')

        self.conn.commit()

    def insert_access_record(self, id_person, date, direction, gate):
        self.cursor.execute('''
            INSERT INTO Access (Id_Person, Date, Direction, Gate) VALUES (?, ?, ?, ?)
        ''', (id_person, date, direction, gate))
        self.conn.commit()

    def calculate_hours_worked(self, date):
        # Implementați logica pentru calculul orelor lucrate
        pass

    def get_employees_list(self):
        self.cursor.execute('SELECT Id, Name FROM Persons')
        return self.cursor.fetchall()
