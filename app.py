from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración para usar SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("/index.html")

@app.route('/opciones_de_usuario')
def opciones_de_usuario():
    return render_template("sub_pages/ingresoORegistroUsuarios.html")

@app.route('/opciones_de_empresa')
def opciones_de_empresa():
    return render_template("sub_pages/ingresoORegistroEmpresas.html")

@app.route("/login_empresas")
def login_empresas():
    return render_template("sub_pages/empresaLoginForm.html")

@app.route("/registro_empresas")
def registro_empresas():
    return render_template("sub_pages/empresaRegisterForm.html")

@app.route("/login_usuarios")
def login_usuarios():
    return render_template("sub_pages/usuariosLoginForm.html")

@app.route("/registro_usuarios")
def registro_usuarios():
    return render_template("sub_pages/usuariosRegisterForm.html")

if __name__ == "__main__":
    app.run(debug=True)