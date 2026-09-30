
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/') 
@app.route('/dashboard')
def dashboard():
   mis_tareas =  [
        {
            "id": 1, "title": "Finalizar maquetado CSS",
            "category": "Frontend",
            "description": "Presentar mi proyecto en la graduación de KodLand",
            "priority": "Alta",
            "status": "Pending",
            "start_date": "05-04-2024"},
        {
            "id": 2,
            "title": "Conectar base de datos SQLite",
            "category": "Backend",
            "description": """To connect Python Script to SQLite, making 
                            available an entire software architecture""",
            "priority": "Alta",
            "status": "Pending",
            "start_date": "20-09-2026"
        },
        {
            "id": 3,
            "title": "Práctica de Listening en Inglés",
            "description": "Listening commedy podcast to practice slang",
            "category": "Estudio",
            "priority": "Media",
            "status": "Pending",
            "start_date": "10-09-2026"
        },
    ]
   return render_template('index.html', tasks=mis_tareas)

if __name__ == "__main__": #Previene ejecución si el archivo solo se esta importando
    app.run(debug=True)