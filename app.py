from flask import Flask, render_template, request , redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/opciones_de_usuario')
def opciones_de_usuario():
    return render_template('sub_pages/ingresoORegistroUsuarios.html')

@app.route('/opciones_de_empresa')
def opciones_de_empresa():
    return render_template('sub_pages/ingresoORegistroEmpresas.html')

@app.route('/registro_usuarios', methods=['GET', 'POST'])
def registro_usuarios():
    if request.method == 'POST':
        # Aquí procesarías el formulario de registro
        # Por ahora, solo redirigimos a la página principal
        return redirect(url_for('index'))
    return render_template('/sub_pages/usuariosRegisterForm.html')

@app.route("/login_usuarios")
def login_usuarios():
    return render_template("/sub_pages/usuariosLoginForm.html")

@app.route("/login_empresas")
def login_empresas():
    return render_template("/sub_pages/empresaLoginForm.html")

@app.route("/registro_empresas")
def registro_empresas():
    return render_template("/sub_pages/empresaRegisterForm.html")

@app.route('/terminos_condiciones_usuarios')
def terminos_condiciones():
    return render_template('terminosCondicionesUsuarios.html')

@app.route('/perfil')
def perfil():
    return render_template('perfilUsuario.html')

if __name__ == '__main__':
    app.run(debug=True)