# Trabajo #1 de Programación Orientado a Objetos.
# Luis Alejandro Salcedo.
from flask import Flask, request, render_template, redirect, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'd94231c751543589c4619656fb1781f28bc9452632e5977ef76660c352bc5da7'

reminders = []
idActual = 1

@app.before_request
def method_override():
    if request.method == "POST" and "_method" in request.form:
        method = request.form["_method"].upper()
        if method in ["PUT", "PATCH", "DELETE"]:
            request.environ["REQUEST_METHOD"] = method

@app.route("/")
def index():
    return render_template("index.html", reminders=reminders)

@app.route("/api/reminders", methods=["GET"])
def api_reminders():
    return reminders, 200

# END POINT: Agregar Recordatorio
@app.route("/api/reminders", methods=["POST"])
def api_add_reminder():
    # Variables
    global idActual
    createdAt = datetime.now().timestamp()

    # Validaciones de campos vacios
    try:
        texto = request.form["content"]
    except ValueError:
        return "El parametro content es obligatorio", 400
    try:
        importante = request.form.get("important")
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

    return redirect("/")

# END POINT: Eliminar Recordatorio
@app.route("/api/reminders/<int:id>", methods=["POST", "DELETE"])
def api_borrar_reminder(id):
    for index, reminder in enumerate(reminders):
        if reminder["id"] == id:
            del reminders[index]
            flash("Recordatorio eliminado exitosamente.", "success")
            return redirect("/")
    flash("Recordatorio no encontrado.", "danger")
    return redirect("/")
