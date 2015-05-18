import sqlite3
import csv 



with sqlite3.connect('oceny.db') as conn:
    conn.execute('''CREATE TABLE oceny (student text, zadanie text, ocena number)''')
    with open('oceny.csv', 'r') as f:
        for row in csv.DictReader(f):
            conn.execute('''insert into oceny(student, zadanie, ocena) values (?, ?, ?)''', (row['student'], row['zadanie'], int(row['ocena'])))
    
            

