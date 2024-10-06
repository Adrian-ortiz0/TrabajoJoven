from flask import Flask, render_template, request, redirect,url_for, flash, session
import re
from models import db, Usuario, Acudiente
from werkzeug.security import generate_password_hash

app = Flask(__name__)

app.secret_key = "7328"  # Necesaria para mostrar mensajes flash

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'  # Base de datos SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
db.init_app(app)

# Crear las tablas al inicializar la app
with app.app_context():
    db.create_all()

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

@app.route("/registro_empresas", methods = ["GET", "POST"])
def registro_empresas():
    if request.method == "POST":
        nombre_encargado = request.form["inputNombre"]
        segundo_nombre_encargado = request.form["inputSegundoNombre"]
        primer_apellido_encargado = request.form["inputPrimerApellido"]
        segundo_apellido_encargado = request.form["inputSegundoApellido"]
        nombre_empresa = request.form["inputNombreDeLaEmpresa"]
        sector = request.form["sector"]
        telefono_empresa = request.form["telefonoEmpresa"]
        correo_empresa = request.form["correoEmpresa"]
        nit_empresa = request.form["nitEmpresa"]
        razon_social = request.form["razonSocialEmpresa"]
        contraseña_empresa = request.form["contraseñaEmpresa"]     
        return render_template("sub_pages/empresaRegisterForm.html")

@app.route("/login_usuarios")
def login_usuarios():
    return render_template("sub_pages/usuariosLoginForm.html")

@app.route('/registro_usuarios', methods=['GET', 'POST'])
def registro_usuarios():
    if request.method == 'POST':  
                
        #Obteniendo los datos del form
        
        nombre_usuario = request.form["inputNombre"]
        segundo_nombre = request.form["inputSegundoNombre"]
        primer_apellido = request.form["inputPrimerApellido"]
        segundo_apellido = request.form["inputSegundoApellido"]
        correo_usuario = request.form["inputCorreoUsuario"]
        telefono_usuario = request.form["inputTelefonoUsuario"]
        genero_usuario = request.form["genero"]
        fecha_nacimiento_usuario = request.form["fechaDeNacimiento"]
        tarjeta_identidad = request.form["tarjetaDeIdentidad"]
        fecha_expedicion_usuario = request.form["fechaDeExpedicion"]
        contraseña_usuario = request.form["contraseñaUsuario"]
        
        # Validar eque los campos mas importantes sean obligatorios
        
        if not nombre_usuario or not primer_apellido or not correo_usuario or not telefono_usuario or not genero_usuario or not fecha_nacimiento_usuario or not tarjeta_identidad or not fecha_expedicion_usuario or not contraseña_usuario:
            flash("Todos los campos obligatorios del usuario deben estar completos.")
            return redirect(url_for('registro_usuarios'))
        
        # Validar el formato del correo electrónico del usuario
        if not re.match(r"[^@]+@[^@]+\.[^@]+", correo_usuario):
            flash("El formato del correo electrónico del usuario es inválido.")
            return redirect(url_for('registro_usuarios'))

        # Validar la longitud de la contraseña del usuario (mínimo 6 caracteres)
        if len(contraseña_usuario) < 6:
            flash("La contraseña del usuario debe tener al menos 6 caracteres.")
            return redirect(url_for('registro_usuarios'))
        
        nombre_titular = request.form['inputNombreTitular']
        segundo_nombre_titular = request.form['inputSegundoNombreTitular']
        apellido_titular = request.form['inputPrimerApellidoTitular']
        segundo_apellido_titular = request.form['inputSegundoApellidoTitular']
        correo_titular = request.form['inputCorreoTitular']
        telefono_titular = request.form['inputTelefonoTitular']
        parentesco_titular = request.form['parentesco']
        fecha_nacimiento_titular = request.form['fechaDeNacimientoTitular']
        cc_titular = request.form['tarjetaDeIdentidadTitular']
        fecha_expedicion_titular = request.form['fechaDeExpedicionTitular']

        if not nombre_titular or not apellido_titular or not correo_titular or not telefono_titular or not parentesco_titular or not fecha_nacimiento_titular or not cc_titular or not fecha_expedicion_titular:
            flash("Todos los campos obligatorios del titular deben estar completos.")
            return redirect(url_for('registro_usuarios'))

        if not re.match(r"[^@]+@[^@]+\.[^@]+", correo_titular):
            flash("El formato del correo electrónico del titular es inválido.")
            return redirect(url_for('registro_usuarios'))
        
        # Guardar los datos en la sesión para usarlos después
        session['user_data'] = {
            "nombre_usuario": nombre_usuario,
            "segundo_nombre": segundo_nombre,
            "primer_apellido": primer_apellido,
            "segundo_apellido": segundo_apellido,
            "correo_usuario": correo_usuario,
            "telefono_usuario": telefono_usuario,
            "genero_usuario": genero_usuario,
            "fecha_nacimiento_usuario": fecha_nacimiento_usuario,
            "tarjeta_identidad": tarjeta_identidad,
            "fecha_expedicion_usuario": fecha_expedicion_usuario,
            "contraseña_usuario": contraseña_usuario,
            "nombre_titular": nombre_titular,
            "segundo_nombre_titular": segundo_nombre_titular,
            "apellido_titular": apellido_titular,
            "segundo_apellido_titular": segundo_apellido_titular,
            "correo_titular": correo_titular,
            "telefono_titular": telefono_titular,
            "parentesco_titular": parentesco_titular,
            "fecha_nacimiento_titular": fecha_nacimiento_titular,
            "cc_titular": cc_titular,
            "fecha_expedicion_titular": fecha_expedicion_titular
        }
        
        #Cuando ya todo sea valido, nos dirigirá a los terminos y condiciones
        
        return redirect(url_for('terminos_condiciones_usuarios'))
    
    return render_template('sub_pages/usuariosRegisterForm.html')

@app.route('/procesar_terminos_condiciones', methods=['POST'])
def procesar_terminos_condiciones():
    acepto = request.form.get('acepto')
    if acepto == "true":
        # Recuperar los datos de la sesión
        user_data = session.get('user_data')

        # Cifrar la contraseña del usuario para seguridad
        hashed_password = generate_password_hash(user_data['contraseña_usuario'], method='pbkdf2:sha256')

        # Crear el registro del acudiente
        nuevo_acudiente = Acudiente(
            nombre=user_data['nombre_titular'],
            segundo_nombre=user_data['segundo_nombre_titular'],
            primer_apellido=user_data['apellido_titular'],
            segundo_apellido=user_data['segundo_apellido_titular'],
            correo=user_data['correo_titular'],
            telefono=user_data['telefono_titular'],
            parentesco=user_data['parentesco_titular'],
            fecha_nacimiento=user_data['fecha_nacimiento_titular'],
            cc_titular=user_data['cc_titular'],
            fecha_expedicion=user_data['fecha_expedicion_titular']
        )
        db.session.add(nuevo_acudiente)
        db.session.commit()

        # Crear el registro del usuario
        nuevo_usuario = Usuario(
            nombre=user_data['nombre_usuario'],
            segundo_nombre=user_data['segundo_nombre'],
            primer_apellido=user_data['primer_apellido'],
            segundo_apellido=user_data['segundo_apellido'],
            correo=user_data['correo_usuario'],
            telefono=user_data['telefono_usuario'],
            genero=user_data['genero_usuario'],
            fecha_nacimiento=user_data['fecha_nacimiento_usuario'],
            tarjeta_identidad=user_data['tarjeta_identidad'],
            fecha_expedicion=user_data['fecha_expedicion_usuario'],
            contraseña=hashed_password,
            acudiente_id=nuevo_acudiente.id
        )
        db.session.add(nuevo_usuario)
        db.session.commit()

        flash("Registro exitoso.")
        return redirect(url_for('perfil'))
    else:
        flash("Debes aceptar los términos y condiciones para continuar.")
        return redirect(url_for('registro_usuarios'))

@app.route('/terminos_condiciones_usuarios')
def terminos_condiciones_usuarios():
    return render_template('sub_pages/terminosCondicionesUsuarios.html')

@app.route('/perfil')
def perfil():
    return render_template('sub_pages/perfilUsuario.html')

@app.route('/admin')
def admin():
    usuarios = Usuario.query.all() 
    return render_template('/admin.html', usuarios=usuarios)

if __name__ == "__main__":
    app.run(debug=True)