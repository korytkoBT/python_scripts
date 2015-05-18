from app import app
from flask import render_template
import sqlite3

def get_oceny(student=None):
    with sqlite3.connect('oceny.db') as conn:
        c = conn.cursor()
        if student is None:
            c.execute('''select student, zadanie, ocena from oceny''')
        else:
            c.execute('''select student, zadanie, ocena from oceny where student = ?''', (student,))
        for row in c:
            yield {'student': row[0], 'zadanie': row[1], 'ocena': row[2]}
            
@app.route('/')
def index():
    return "Hello world"
@app.route('/oceny')
def oceny():
    return render_template('oceny.html', title='Oceny', oceny=get_oceny())

@app.route('/oceny/<student>')
def filtered_oceny(student):
    return render_template('oceny.html', title='Oceny', oceny=get_oceny(student))
