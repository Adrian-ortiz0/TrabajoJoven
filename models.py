from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    segundo_nombre = db.Column(db.String(100))
    primer_apellido = db.Column(db.String(100), nullable=False)
    segundo_apellido = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(120), unique=True, nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    genero = db.Column(db.String(20))
    fecha_nacimiento = db.Column(db.String(10))
    tarjeta_identidad = db.Column(db.String(20), nullable=False, unique=True)
    fecha_expedicion = db.Column(db.String(10), nullable=False)
    contraseña = db.Column(db.String(200), nullable=False)
    foto_perfil = db.Column(db.String(200))
    
    # Relaciones
    acudiente_id = db.Column(db.Integer, db.ForeignKey('acudiente.id'))

class Acudiente(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    segundo_nombre = db.Column(db.String(100))
    primer_apellido = db.Column(db.String(100), nullable=False)
    segundo_apellido = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(120), unique=True, nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    parentesco = db.Column(db.String(50), nullable=False)
    fecha_nacimiento = db.Column(db.String(10), nullable=False)
    cc_titular = db.Column(db.String(20), nullable=False, unique=True)
    fecha_expedicion = db.Column(db.String(10), nullable=False)

    # Relación inversa (un usuario tiene un acudiente)
    usuario = db.relationship('Usuario', backref='acudiente')
