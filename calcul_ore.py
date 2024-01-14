from datetime import datetime
from access_gate import AccessGate
from constants import DB_NAME
from database import AccessDatabase

def test_gate_processing():
    # Test 1.1
    access_gate_1 = AccessGate(1, 'intrari')
    access_gate_2 = AccessGate(2, 'intrari')
    access_gate_1.process_files()
    access_gate_2.process_files()

    # Test 1.2
    # Verificare  directorul backup_intrari și conținutul său

def test_employee_creation():
    # Test 2.1
    database = AccessDatabase()
    database.calculate_hours_worked(datetime.now().date())

    # Test 2.2
    for _ in range(10):
        pass
    # Verificare manual baza de date pentru datele inserate

def test_hours_calculation():
    # Test 3.1
    database = AccessDatabase()
    database.calculate_hours_worked(datetime.now().date())
    # Verificare manual rezultatele

if __name__ == "__main__":
    test_gate_processing()
    test_employee_creation()
    test_hours_calculation()
