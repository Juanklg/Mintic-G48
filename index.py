from flask import Flask, render_template
import funciones as fn

app = Flask(__name__)

fn.isLogin("Login")
var = "Corriendo la app"
# --------------------------------------------------------------------------------
@app.route("/")
def hello_world():
    return "Hola Grupo 48"

@app.route("/proyecto")
def proyecto():
    return render_template("index.html")

# rut = r"C:\Users\MakeDream\Desktop\Ruta1\Mintic-G48\dbTask.xlsx"
# Tablas = crud.consultarTablas(rut)
# fn.detailVar(Tablas)

if __name__ == '__main__':
    app.run(debug=True)#el debug = true es para trabajar en desarrollo