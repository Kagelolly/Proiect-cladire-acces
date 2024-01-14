class AccessDatabase:
    # ...

    def calculate_hours_worked(self, date):
        # Obțineți toate înregistrările pentru data specificată
        self.cursor.execute('SELECT Id_Person, Date, Direction FROM Access WHERE Date BETWEEN ? AND ?', (date, date))
        records = self.cursor.fetchall()

        for person_id, records_for_date in groupby(records, key=lambda x: x[0]):
            # Sortați înregistrările după oră
            sorted_records = sorted(records_for_date, key=lambda x: x[1])

            # Logica pentru cazurile speciale ale orelor de lucru
            # ...

            # Calculați numărul total de ore lucrate
            total_hours_worked = calculate_total_hours(sorted_records)

            # Salvați rezultatele în tabela WorkedHours
            self.cursor.execute('INSERT OR REPLACE INTO WorkedHours (Id_Person, Date, HoursWorked) VALUES (?, ?, ?)',
                                (person_id, date, total_hours_worked))

        self.conn.commit()
