from Gestion_prestamos.configuracion_base_datos import conectar, desconectar

class Curso:
    def __init__(self, curso, nivel):
        self.curso = curso
        self.nivel = nivel

    def obtener_todos_cursos(self):
        conexion = conectar()
        if conexion is not None:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM cursos")
            cursos = cursor.fetchall()
            cursor.close()
            desconectar(conexion)
            return cursos
        return None

    def obtener_un_curso(self, curso):
        conexion = conectar()
        if conexion is not None:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM cursos WHERE curso = %s", (curso,))
            curso = cursor.fetchone()
            cursor.close()
            desconectar(conexion)
            return curso
        return None

    def insertar_curso(self):
        conexion = conectar()
        if conexion is not None:
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO cursos (curso, nivel) VALUES (%s, %s)",
                           (self.curso, self.nivel))
            conexion.commit()
            cursor.close()
            desconectar(conexion)
            print("Curso creado correctamente")