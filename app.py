from flask import Flask, request, render_template, redirect, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'd94231c751543589c4619656fb1781f28bc9452632e5977ef76660c352bc5da7'

reminders = []
idActual = 1

@app.route("/")
def index():
    return render_template("index.html", reminders=reminders)

@app.route("/api/reminders", methods=["GET"])
def api_reminders():
    return reminders, 200

# END POINT: Agregar Recordatorio
@app.route("/api/reminders", methods=["POST"])
def api_add_reminder():
    global idActual
    createdAt = datetime.now().timestamp()

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

    if importante is None:
        importante = False
    elif importante == "true" or importante == "True":
        importante = True
    elif importante == "false" or importante == "False":
        importante = False
    else:
        return "El valor de important debe ser True o False", 400

    new_reminder = { "id": idActual, "content": texto, "important": importante, "createdAt": createdAt }
    reminders.append(new_reminder)
    idActual += 1
    reminders.sort(key=lambda x: not x["important"])
    return redirect("/")

# END POINT: Actualizar Recordatorio
@app.route("/api/reminders/<int:id>", methods=["POST", "PATCH"])
def actualizar_reminder(id):
    content = request.form.get("content", "").strip()
    important = request.form.get("important", "false").lower()

    for reminder in reminders:
        if reminder["id"] == id:
            if content:
                if len(content) > 120:
                    flash("El contenido no puede superar los 120 caracteres", "danger")
                    return redirect("/")
                reminder["content"] = content

            if important == "true":
                reminder["important"] = True
            elif important == "false":
                reminder["important"] = False
            else:
                flash("El valor de 'importante' debe ser True o False", "danger")
                return redirect("/")
            reminders.sort(key=lambda x: not x["important"])
            flash("Recordatorio actualizado exitosamente", "success")
            return redirect("/")

    flash("Recordatorio no encontrado", "danger")
    return redirect("/")

# END POINT: Borrar Recordatorio
@app.route("/api/reminder/<int:id>", methods=["POST", "DELETE"])
def borrar_reminder(id):
    for index, reminder in enumerate(reminders):
        if reminder["id"] == id:
            del reminders[index]
            flash("Recordatorio eliminado exitosamente.", "success")
            return redirect("/")
    flash("Recordatorio no encontrado.", "danger")
    return redirect("/")

# END POINT: Borrar Recordatorio (API)
@app.route("/api/reminders/<int:id>", methods=["DELETE"])
def api_borrar_reminder(id):
    for index, reminder in enumerate(reminders):
        if reminder["id"] == id:
            del reminders[index]
            flash("Recordatorio eliminado exitosamente.", "success")
            return redirect("/")
    flash("Recordatorio no encontrado.", "danger")
    return redirect("/")
