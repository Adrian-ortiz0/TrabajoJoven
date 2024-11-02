from flask import Flask, render_template, request, redirect,url_for, flash, session
import re
import os
from models import db, Usuario, Acudiente
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from werkzeug.utils import secure_filename

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

@app.route("/login_usuarios", methods = ["GET", "POST"])
def login_usuarios():
    if request.method == "POST":
        correo = request.form.get("inputCorreoUsuario")
        contraseña = request.form.get("contraseñaUsuario")
        
        # Buscar al usuario en la base de datos
        usuario = Usuario.query.filter_by(correo=correo).first()
        
        if usuario and check_password_hash(usuario.contraseña, contraseña):
            # Si las credenciales son correctas, iniciar sesión
            session['usuario_id'] = usuario.id  # Guardar el ID del usuario en la sesión
            flash(f"Bienvenido, {usuario.nombre}!")
            return redirect(url_for('perfil'))  # Redirigir al perfil del usuario
        else:
            # Si las credenciales no son válidas, mostrar un mensaje de error
            flash("Correo o contraseña incorrectos.")
            return redirect(url_for('login_usuarios'))  # Redirigir al formulario de login
        
    return render_template("sub_pages/usuariosLoginForm.html")

def login_requerido(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        # Verificar si el usuario ha iniciado sesión
        if 'usuario_id' not in session:
            flash("Debes iniciar sesión para acceder a esta página.")
            return redirect(url_for('login_usuarios'))  # Redirigir al login si no está autenticado
        return f(*args, **kwargs)
    return wrap

# ----------------------------------------------------------------------------------------------------------------

# Creacion de la funcion para subir imagenes

# Configura la carpeta donde se guardarán las imágenes
UPLOAD_FOLDER = 'static/uploads'  # Asegúrate de que esta carpeta exista
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Asegúrate de que el tamaño máximo del archivo no sea demasiado grande
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB

@app.route('/subir_foto_perfil', methods=['POST'])
@login_requerido
def subir_foto_perfil():
    if 'foto_perfil' not in request.files:
        flash('No se seleccionó ningún archivo')
        return redirect(url_for('perfil'))

    archivo = request.files['foto_perfil']
    
    if archivo.filename == '':
        flash('No se seleccionó ningún archivo')
        return redirect(url_for('perfil'))

    # Asegúrate de que el archivo sea seguro para ser guardado
    filename = secure_filename(archivo.filename)
    archivo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    # Aquí podrías guardar la ruta de la imagen en la base de datos, asociándola al usuario
    usuario = Usuario.query.get(session['usuario_id'])
    usuario.foto_perfil = filename  # Asumiendo que tienes un campo `foto_perfil` en tu modelo Usuario
    db.session.commit()

    flash('Foto de perfil actualizada con éxito')
    return redirect(url_for('perfil'))

# -----------------------------------------------------------------------------------------------------------------

@app.route('/registro_usuarios', methods=['GET', 'POST'])
def registro_usuarios():
    if request.method == 'POST':  
                
        #Obteniendo los datos del form
        
        nombre_usuario = request.form.get("inputNombre")
        segundo_nombre = request.form.get("inputSegundoNombre")
        primer_apellido = request.form.get("inputPrimerApellido")
        segundo_apellido = request.form.get("inputSegundoApellido")
        correo_usuario = request.form.get("inputCorreoUsuario")
        telefono_usuario = request.form.get("inputTelefonoUsuario")
        genero_usuario = request.form.get("genero")
        fecha_nacimiento_usuario = request.form.get("fechaDeNacimiento")
        tarjeta_identidad = request.form.get("tarjetaDeIdentidad")
        fecha_expedicion_usuario = request.form.get("fechaDeExpedicion")
        contraseña_usuario = request.form.get("contraseñaUsuario")
        
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
        
        # Obteniendo los datos del titular/acudiente
        nombre_titular = request.form.get('inputNombreTitular')
        segundo_nombre_titular = request.form.get('inputSegundoNombreTitular')
        apellido_titular = request.form.get('inputPrimerApellidoTitular')
        segundo_apellido_titular = request.form.get('inputSegundoApellidoTitular')
        correo_titular = request.form.get('inputCorreoTitular')
        telefono_titular = request.form.get('inputTelefonoTitular')
        parentesco_titular = request.form.get('parentesco')
        fecha_nacimiento_titular = request.form.get('fechaDeNacimientoTitular')
        cc_titular = request.form.get('tarjetaDeIdentidadTitular')
        fecha_expedicion_titular = request.form.get('fechaDeExpedicionTitular')

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
        return redirect(url_for('index'))
    
@app.route('/editarPerfilUsuario')
@login_requerido
def editarPerfilUsuario():
    usuario = Usuario.query.get(session['usuario_id'])  # Cambia esto según cómo desees recuperar al usuario
    if usuario is None:
        return "No hay usuarios registrados."  # O redirigir a otra página o mostrar un mensaje adecuado.
    
    return render_template('sub_pages/editarPerfilUsuario.html', usuario=usuario)

@app.route('/terminos_condiciones_usuarios')
def terminos_condiciones_usuarios():
    return render_template('sub_pages/terminosCondicionesUsuarios.html')

@app.route('/logout', methods=['POST'])
@login_requerido
def logout():
    session.clear()
    flash('Has cerrado sesión correctamente')
    return redirect(url_for('index'))

@app.route('/perfil')
@login_requerido
def perfil():
    usuario = Usuario.query.get(session['usuario_id'])  # Recuperar el usuario que está en sesión
    return render_template('sub_pages/perfilUsuario.html', usuario=usuario)

@app.route('/admin')
@login_requerido
def admin():
    usuarios = Usuario.query.all()  # Listar todos los usuarios
    return render_template('/admin.html', usuarios=usuarios)

if __name__ == "__main__":
    app.run(debug=True)