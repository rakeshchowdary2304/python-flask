from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, value TEXT)''')
    conn.commit()
    conn.close()

# Insert data into the database
def insert_data(value):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO data (value) VALUES (?)', (value,))
    conn.commit()
    conn.close()

# Fetch all data from the database
def fetch_data():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT value FROM data')
    data = c.fetchall()
    conn.close()
    return [item[0] for item in data]

# Home route
@app.route('/')
def index():
    data = fetch_data()
    return render_template('index.html', data=data)

# Route to handle form submission
@app.route('/add-data', methods=['POST'])
def add_data():
    data = request.form['data']
    insert_data(data)
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
