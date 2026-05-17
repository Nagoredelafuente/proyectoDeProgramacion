from Gestion_prestamos.configuracion_base_datos import conectar, desconectar

class Materia():
    def __init__(self, nombre, departamento):
        self.nombre = nombre
        self.departamento = departamento

    def obtener_todas_materias(self):
        conexion = conectar()
        if conexion is not None:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM materias")
            materias = cursor.fetchall()
            cursor.close()
            desconectar(conexion)
            return materias
        return None

    def obtener_una_materia(self, id):
        conexion = conectar()
        if conexion is not None:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM materias WHERE id = %s", (id,))
            materia = cursor.fetchone()
            cursor.close()
            desconectar(conexion)
            return materia
        return None

    def insertar_materia(self):
        conexion = conectar()
        if conexion is not None:
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO materias (nombre, departamento) VALUES (%s, %s)",
                           (self.nombre, self.departamento))
            conexion.commit()
            cursor.close()
            desconectar(conexion)
            print("Materia creada con exito")