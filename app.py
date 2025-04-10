# Trabajo #1 de Programación Orientado a Objetos.
# Luis Alejandro Salcedo.
from flask import Flask, request, render_template, redirect, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'd94231c751543589c4619656fb1781f28bc9452632e5977ef76660c352bc5da7'

reminders = []
idActual = 1

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/reminders", methods=["GET"])
def api_reminders():
    return reminders, 200

# END POINT: Agregar Recordatorio
@app.route("/api/reminders", methods=["POST"])
def api_add_reminder():
    # Variables
    global idActual
    datos = request.get_json()
    createdAt = datetime.now().timestamp()

    # Validaciones de campos vacios
    try:
        texto = datos.get("content")
    except ValueError:
        return "El parametro content es obligatorio", 400
    try:
        importante = datos.get("important")
    except ValueError:
        importante = None
    if len(texto) > 120:
        return "El content no puede superar 120 caracteres", 400
    if texto.strip() == "":
        return "El content no puede estar vacío", 400

    # Validacion de Important
    if importante is None:
        importante = False
    elif importante == "true" or importante == "True":
        importante = True
    elif importante == "false" or importante == "False":
        importante = False
    else:
        return "El valor de important debe ser True o False", 400

    # Agregar recordatorio
    new_reminder = { "id": idActual, "content": texto, "important": importante, "createdAt": createdAt }
    reminders.append(new_reminder)
    idActual += 1

    return new_reminder, 201