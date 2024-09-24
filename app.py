from flask import Flask, render_template, redirect, url_for, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/usuarios')
def usuarios():
    return render_template('sub_pages/usuarios.html')

@app.route('/empresas')
def empresas():
    return render_template('sub_pages/empresas.html')

@app.route('/terminos-condiciones')
def terminos_condiciones():
    return render_template('sub_pages/terminosCondicionesUsuarios.html')

@app.route('/perfil-usuario')
def perfil_usuario():
    return render_template('sub_pages/perfilUsuario.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    return jsonify({"success": True, "message": f"Bienvenido, {username}!"})

if __name__ == '__main__':
    app.run(debug=True)