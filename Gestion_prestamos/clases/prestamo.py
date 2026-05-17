from Gestion_prestamos.configuracion_base_datos import conectar,desconectar

class Prestamo():
    def __init__(self, nie, curso, isbn, fecha_entrega, fecha_devolucion, estado):
        self.nie = nie
        self.curso = curso
        self.isbn = isbn
        self.fecha_entrega = fecha_entrega
        self.fecha_devolucion = fecha_devolucion
        self.estado = estado

    def obtener_todos_prestamos(self):
        conexion = conectar()
        if conexion is not None:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM prestamos")
            prestamos = cursor.fetchall()
            cursor.close()
            desconectar(conexion)
            return prestamos
        return None

    def obtener_por_alumno(self, nie):
        conexion = conectar()
        if conexion is not None:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM prestamos WHERE nie = %s", (nie,))
            prestamos = cursor.fetchall()
            cursor.close()
            desconectar(conexion)
            return prestamos
        return None

    def asignar_prestamo(self):
        conexion = conectar()
        if conexion is not None:
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO prestamos (nie, curso, isbn, fecha_entrega, fecha_devolucion, estado)"
                           " VALUES (%s, %s, %s, %s, %s, %s)",
                           (self.nie, self.curso, self.isbn, self.fecha_entrega, self.fecha_devolucion, self.estado))
            conexion.commit()
            cursor.close()
            desconectar(conexion)
            print("Prestamo asignado con exito")

    def cerrar_prestamo(self, nie, isbn):
        conexion = conectar()
        if conexion is not None:
            cursor = conexion.cursor()
            cursor.execute("UPDATE prestamos SET estado = 'D', fecha_devolucion = CURDATE() "
                           "WHERE nie = %s AND isbn = %s",
                           (nie, isbn))
            conexion.commit()
            cursor.close()
            desconectar(conexion)
            print("Prestamo cerrado con exito")

    def generar_contrato(self, nie):
        conexion = conectar()
        if conexion is not None:
            cursor = conexion.cursor()
            cursor.execute("SELECT a.nombre, a.apellidos, l.titulo, l.autor, "
                           "p.fecha_entrega, p.fecha_devolucion, p.estado "
                           "FROM prestamos p "
                           "JOIN alumnos a ON p.nie = a.nie "
                           "JOIN libros l ON p.isbn = l.isbn "
                           "WHERE p.nie = %s", (nie,))
            contrato = cursor.fetchall()
            cursor.close()
            desconectar(conexion)
            return contrato
        return None

