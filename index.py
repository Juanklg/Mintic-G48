import funciones as fn
from flask import Flask, render_template,request
fn.isLogin("Login")
var = "Iniciando".center(50,'-')
app = Flask(__name__)
# --------------------------------------------------------------------------------
@app.route("/")
def Eindex():
    return render_template("index.html",title='wordSelector')# formulario de inicio

@app.route("/login")
def Elogin(username=None):
    user=request.args['username']
    return render_template("user.html",title='wordSelector',user=user)# formulario de inicio

@app.route("/registro")
def Eregistro():
    return render_template("registro.html")#formulario de registro

@app.route("/admin")
def Eadmin():
    return render_template("admin.html")#formulario de edicion o activacion

@app.route("/usuarios/<name>")
def Euser(name=None):
    print(f'---------capturado user {name}')
    # listas = fn.listas_d
    return render_template("user.html",user=name)

# @app.route("/proyecto/<p>")
# def proy(p=None):
#     proyecto=fn.getProyectoByUser(p)    
#     return render_template("proyecto.html",proyecto=proyecto,w=600)

# --------------------------------------------------------------------------------
# Vistas documentacion
@app.route("/doc")
def Edoc():
    return render_template(f"doc/doc.html",title='Documentacion')
@app.route("/doc/<doc>")
def Edocu(doc=None):
    return render_template(f"doc/{doc}.html")

print("Imprimiendo variable dunder name en main = ",__name__)
if __name__ == '__main__':
    app.run(debug=True)