import sqlite3
from tabulate import tabulate
from random import choice
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

# Connect to the database
conn = sqlite3.connect('problems.db')
c = conn.cursor()

c.execute('''
            SELECT * FROM PROBLEMS;
''')

rows = c.fetchall()
headers = [desc[0] for desc in c.description]

# print(choice(rows))
print(tabulate(rows, headers=headers, tablefmt='heavy_grid'))

conn.commit()
conn.close()

