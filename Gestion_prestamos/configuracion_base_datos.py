import mysql.connector

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="prestamos_libros"
        )
        return conexion
    except mysql.connector.Error as error:
        print("Error conectando con base de datos", error)
        return None

def desconectar(conexion):
    try:
        if conexion.is_connected():
            conexion.close()
            print("Conexion cerrada con exito")
    except mysql.connector.Error as error:
        print("Error al cerrar la base de datos", error)