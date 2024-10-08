CREATE DATABASE IF NOT EXISTS TRABAJO_JOVEN;
USE TRABAJO_JOVEN;

-- Tabla de Acudientes
CREATE TABLE IF NOT EXISTS Acudiente(
	Id_Acudiente INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(50) NOT NULL,
    Segundo_Nombre VARCHAR(50),
    Apellido VARCHAR(50) NOT NULL,
    Segundo_Apellido VARCHAR(50),
    Correo VARCHAR(50) UNIQUE NOT NULL,
    Telefono VARCHAR(50) NOT NULL,
    Parentesco ENUM("Padre", "Madre", "Otro") NOT NULL,
    Fecha_Nacimiento DATE NOT NULL,
    Cedula VARCHAR(50) NOT NULL,
    Fecha_Expedicion DATE NOT NULL-
);

-- Tabla de Usuarios
CREATE TABLE IF NOT EXISTS Usuarios(
	Id_Usuario INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(50) NOT NULL,
    Segundo_Nombre VARCHAR(50),
    Apellido VARCHAR(50) NOT NULL,
    Segundo_Apellido VARCHAR(50),
    Correo VARCHAR(50) UNIQUE NOT NULL,
    Telefono VARCHAR(50) NOT NULL,
    Genero ENUM("M", "F", "Otro") NOT NULL,
    Fecha_Nacimiento DATE NOT NULL,
    Tarjeta_Identidad VARCHAR(50) NOT NULL,
    Fecha_Expedicion DATE NOT NULL,
    Contraseña VARCHAR(50) NOT NULL,
    Estado ENUM("Contratado", "No empleado"),
    Id_Acudiente INT,
    FOREIGN KEY (Id_Acudiente) REFERENCES Acudiente (Id_Acudiente)
);

-- Tabla de Representantes
CREATE TABLE IF NOT EXISTS Representantes(
	Id_Representante INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(50) NOT NULL,
    Segundo_Nombre VARCHAR(50),
    Apellido VARCHAR(50) NOT NULL,
    Segundo_Apellido VARCHAR(50),
    Correo VARCHAR(50) UNIQUE NOT NULL,
    Telefono VARCHAR(50) NOT NULL,
    Contraseña VARCHAR(50) NOT NULL
);

-- Tabla de Empresas
CREATE TABLE IF NOT EXISTS Empresas(
	Id_Empresa INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(150) NOT NULL,
    Sector VARCHAR(150) NOT NULL,
    Telefono VARCHAR(150) NOT NULL,
    Correo VARCHAR(150) UNIQUE NOT NULL,
    Nit VARCHAR(50) NOT NULL,
    Razon_Social VARCHAR(150) NOT NULL,
    Id_Representante INT,
    FOREIGN KEY (Id_Representante) REFERENCES Representantes (Id_Representante)
);

-- Tabla de Vacantes
CREATE TABLE IF NOT EXISTS Vacantes(
	Id_Vacante INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(100) NOT NULL,
    Fecha_Publicacion DATE NOT NULL,
    Estado BOOLEAN NOT NULL DEFAULT (FALSE),
    Descripcion TEXT,
	Id_Empresa INT,
    FOREIGN KEY (Id_Empresa) REFERENCES Empresas(Id_Empresa)
);

-- Relación entre Vacantes y Empresas
CREATE TABLE IF NOT EXISTS VacantesEmpresas(
	Id_Vacante INT,
    Id_Empresa INT,
    PRIMARY KEY(Id_Vacante, Id_Empresa),
    FOREIGN KEY (Id_Vacante) REFERENCES Vacantes (Id_Vacante),
    FOREIGN KEY (Id_Empresa) REFERENCES Empresas (Id_Empresa)
);

-- Relación entre Postulaciones
CREATE TABLE IF NOT EXISTS Postulacion(
    Id_Usuario INT,
    Id_Vacante INT,
    Estado ENUM('Pendiente', 'Aceptado', 'Rechazado') DEFAULT 'Pendiente',
    Fecha_Postulacion DATE NOT NULL,
    PRIMARY KEY(Id_Vacante, Id_Usuario),
    FOREIGN KEY (Id_Vacante) REFERENCES Vacantes(Id_Vacante),
    FOREIGN KEY (Id_Usuario) REFERENCES Usuarios(Id_Usuario)
);