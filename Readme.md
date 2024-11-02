# Trabajo Joven

Trabajo joven es un proyecto realizado en Python, especificamente usando el framework de Flask, este proyecto esta siendo realizado unicamente con fines de poder aprender y dominar este framework de python. Este proyecto actualemte se encuentra en desarrollo, ya que faltan muchas otras funcionalidades por agregar, sin embargo, el proyecto recibe actualizaciones de manera constante con el fin de poder dejar totalemte funcional esta aplicación.

## Tabla de contenido 🚀

| Indice | Titulo          |
| ------ | --------------- |
| 1      | Instalación     |
| 2      | Estructura de la Base de Datos  |
| 3      | Diagrama EDR    |
| 4      | Uso   |
| 5      | funcionalidades |
| 6      | FAQs            |
| 7      | Licencia        |
| 8      | Creador         |

## Instalación 📐

Clona el proyecto

```bash
  git clone https://github.com/Adrian-ortiz0/TrabajoJoven
```

Ve al directorio del proyecto

```bash
  cd TrabajoJoven
```

Ir al archivo

```bash
  code .
```

## Estructura de la base de Datos ℹ️

1. **Tabla Acudientes**

La tabla acudientes pedirá los datos necesarios para poder comprobar la existencia de un acudiente para cada usaurio.

2. **Tabla de Usuarios**

La tabla usuarios tendra una relacion directa con la tabla acudientes, debido a que cada usaurio puede tener un acudiente.

3. **Tabla de Empresas**

La tabla de empresas pedirá datos relacionados con los documentos necesarios para verificar la existencia de esta misma y se pedirá directamente la representación de alguna persona de la empresa.

4. **Tabla de Vacantes**

La tabla vacantes hará una relacion de muchos a muchos con los empresas, ya que muchas empresas pueden publicar muchas vacantes.

5. **Detalles de vacantes**

Esta tabla se encarga de relacionar muchas empresas con muchas vacantes, cumpliendo asi con los requisitos establecidos para la aplicación.

6. **Postulaciones**

Esta tabla sirve para dar detalles de las postulaciones relacionadas con los usuarios.

7. **Detalles postulaciones**

Tabla encargada de conectar con postulaciones y los usuarios para poder garantizar la relacion de muchos a muchos.

## Diagrama EDR 🖼️

## Usos 🏗️ (Actualmente se sigue trabajando en cada uno de estos)

En la aplicacion se pueden realizar las siguientes acciones:

1. Registrar usuarios y empresas.
2. Loggear usuarios y empresas.
3. Editar datos de los usuarios y las empresas.
4. Subir sus fotos de perfiles.
5. Subida de curriculums para los usuarios.
6. Almacenamiento de la información en SQLite.
7. Publicacion de vacantes por parte de las empresas.
8. Postulacion a vacantes publicadas por las empresas.
9. Guardar empresas como tus favoritas.

## Funcionalidades 👷 (Se siguen actualizando y mejorando)

Entre las funcionalidades mas destacables e importantes de la aplicación, podemos encontrar:

* Cambio de foto de perfil.
* Postulacion a vacantes.
* Publicacion de vacantes.
* Inicio y cierre de sesión.
* Registros.
* Comprobacion de edades y fechas.
* Subida de documentos importantes.

## FAQs

#### ¿Como puedo aportar al proyecto?

Puedes comunicarte conmigo, el dueño del repositorio y tomaré en cuanta cada recomendacion, para comunicarte conmigo puedes hacerlo a través de mi correo electronico: dxniel7328@gmail.com.

#### ¿Ya esta desplegada y terminada la aplicación?

No, actualmente la aplicación se encuentra en desarrollo, futuramente se podrá desplegar se le harán actualizaciones de manera semanal para garantzar su mantenimiento.

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)

## Creador

- [@Adrian-ortiz0](https://github.com/Adrian-ortiz0)

Basado en las ideas de Yuli Stefany Sanchez Santos.