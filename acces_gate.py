import os
from datetime import datetime
from constants import DB_NAME
from database import AccessDatabase

class AccessGate:
    def __init__(self, gate_number, input_directory):
        self.gate_number = gate_number
        self.input_directory = input_directory
        self.database = AccessDatabase()

    def process_files(self):
        for filename in os.listdir(self.input_directory):
            if filename.startswith(f'Poarta{self.gate_number}.'):
                file_path = os.path.join(self.input_directory, filename)
                self.read_file(file_path)
                self.move_file(file_path)

    def read_file(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                id_person, date_str, direction = int(parts[0]), parts[1], parts[2]
                date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%fZ')
                self.database.insert_access_record(id_person, date, direction, self.gate_number)

    def move_file(self, file_path):
        backup_directory = os.path.join(os.path.dirname(file_path), 'backup_intrari')
        os.makedirs(backup_directory, exist_ok=True)
        new_filename = f'{file_path.replace(os.path.sep, "_")}_{datetime.now().strftime("%Y%m%d%H%M%S")}'
        new_path = os.path.join(backup_directory, new_filename)
        os.rename(file_path, new_path)

if __name__ == "__main__":
    gate_number = 1
    input_directory = '/cale/catre/fisier'
    access_gate = AccessGate(gate_number, input_directory)
    access_gate.process_files()
