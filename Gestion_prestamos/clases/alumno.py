from Gestion_prestamos.configuracion_base_datos import conectar, desconectar

class Alumno:
    def __init__(self, nie, nombre, apellidos, tramo, bilingue):
        self.nie = nie
        self.nombre = nombre
        self.apellidos = apellidos
        self.tramo = tramo
        self.bilingue = bilingue

    def obtener_todos_alumnos(self):
        conexion = conectar()
        if conexion is not None:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM alumnos")
            alumnos = cursor.fetchall()
            cursor.close()
            desconectar(conexion)
            return alumnos

    def obtener_un_alumno(self, nie):
        conexion = conectar()
        if conexion is not None:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM alumnos WHERE nie= %s", (nie,))
            alumno = cursor.fetchone()
            cursor.close()
            desconectar(conexion)
            return alumno
        return None

    def insertar_alumno(self):
        conexion = conectar()
        if conexion is not None:
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO alumnos (nie, nombre, apellidos, tramo, bilingue) "
                           "VALUES (%s, %s, %s, %s, %s)",
                           (self.nie, self.nombre, self.apellidos, self.tramo,self.bilingue))
            conexion.commit()
            cursor.close()
            desconectar(conexion)
            print("Alumno insertado con exito.")

    def modificar_alumno(self):
        conexion = conectar()
        if conexion is not None:
            cursor = conexion.cursor()
            cursor.execute("UPDATE alumnos SET nombre = %s, apellidos = %s, tramo = %s, bilingue = %s "
                           "WHERE nie = %s",
                           (self.nombre, self.apellidos, self.tramo, self.bilingue, self.nie))
            conexion.commit()
            cursor.close()
            desconectar(conexion)
            print("Alumno modificado con exito.")