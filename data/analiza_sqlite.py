import sqlite3

with sqlite3.connect('oceny.db') as conn:
    c = conn.cursor()
    c.execute('''select * from oceny where student in (select student from oceny group by student order by avg(ocena)  desc limit 3)''')
    for row in c:
        print row
