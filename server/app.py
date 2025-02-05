from flask import Flask, request, jsonify, render_template
import sqlite3
from datetime import datetime

app = Flask(__name__)
DATABASE = 'metrics.db'

# Создание базы данных
def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            agent_id TEXT,
            cpu_load REAL,
            ram_usage REAL,
            disk_usage REAL
        )''')

# Маршрут для получения данных от агентов
@app.route('/api/metrics', methods=['POST'])
def receive_metrics():
    data = request.json
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('INSERT INTO metrics (agent_id, cpu_load, ram_usage, disk_usage) VALUES (?, ?, ?, ?)', 
                     (data['agent_id'], data['cpu_load'], data['ram_usage'], data['disk_usage']))
    return jsonify({"status": "success"}), 200

# Веб-интерфейс
@app.route('/')
def dashboard():
    with sqlite3.connect(DATABASE) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.execute('SELECT * FROM metrics ORDER BY timestamp DESC LIMIT 50')
        data = [dict(row) for row in cursor.fetchall()]
    return render_template('dashboard.html', metrics=data)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
