
from flask import Flask,render_template,request,session,url_for
from werkzeug.utils import redirect
import funciones.user as fn
app = Flask(__name__)

# user=request.args['username']
    # print(request.form)
    # data = fn.getDataUser('user')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    fn.printUsers()
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(type(request))
        session['username'] = request.form['username']
        fn.login(request.form)
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route("/registro")
def Eregistro():    
    html = render_template("registro.html")#formulario de registro
    return render_template("dinamico.html",html=html)

@app.route("/admin")
def Eadmin():
    return render_template("admin.html")#formulario de edicion o activacion

@app.route("/usuarios/<name>")
def Euser(name=None):
    print(f'---------capturado user {name}')
    # listas = fn.listas_d
    return render_template("user.html",user=name)

# app.run(debug=True)
# hacer configuracion para usar modo desarrollo, cambia variable de entorno a desarrollo con el siguiente comando:
# export FLASK_ENV=development
