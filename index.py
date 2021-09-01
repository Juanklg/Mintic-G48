from flask import Flask, render_template
import funciones as fn
# from numpy import random as r
import numpy as np

app = Flask(__name__)

fn.isLogin("Login")
var = "Corriendo la app"
# --------------------------------------------------------------------------------
@app.route("/usuarios/<name>")
def hello_world(name=None):    
    user = fn.returnUser(name)
    return render_template("user.html",user=user)

@app.route("/")
def proyecto():
    return render_template("index.html")

# rut = r"C:\Users\MakeDream\Desktop\Ruta1\Mintic-G48\dbTask.xlsx"
# Tablas = crud.consultarTablas(rut)
# fn.detailVar(Tablas)

print("Imprimiendo variable dunder name en funciones = ",__name__)
if __name__ == '__main__':
    app.run(debug=True)