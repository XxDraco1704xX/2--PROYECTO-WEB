
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
@app.route('/dashboard')
def dashboard():
    mis_tareas = [
        {'title': 'Crear base de datos', 'priority': 'high'},
        {'title': 'Diseñar interfaz', 
         'description': 'To be able to save data permanently', 'priority': 'medium'}
    ]
    return render_template('index.html', tasks=mis_tareas)
