from Gestion_prestamos.configuracion_base_datos import conectar, desconectar

class Libros:
    def __init__(self, isbn, titulo, autor, numero_ejemplares, id_materia, id_curso):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.numero_ejemplares = numero_ejemplares
        self.id_materia = id_materia
        self.id_curso = id_curso

    def obtener_todos_libros(self):
        conexion = conectar()
        if conexion is not None:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM libros")
            libros = cursor.fetchall()
            cursor.close()
            return libros
        return None

    def obtener_un_libro(self, isbn):
        conexion = conectar()
        if conexion is not None:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM libros WHERE isbn = %s", (isbn,))
            libro = cursor.fetchone()
            cursor.close()
            desconectar(conexion)
            return libro
        return None

    def insertar_libro(self):
        conexion = conectar()
        if conexion is not None:
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO libros (isbn, titulo, autor, numero_ejemplares, id_materia, id_curso) "
                           "VALUES (%s, %s, %s, %s, %s, %s)",
                           (self.isbn, self.titulo, self.autor, self.numero_ejemplares, self.id_materia, self.id_curso))
            conexion.commit()
            cursor.close()
            desconectar(conexion)
            print("Libro insertado correctamente")

    def modificar_libro(self):
         conexion = conectar()
         if conexion is not None:
             cursor = conexion.cursor()
             cursor.execute("UPDATE libros SET titulo = %s, autor = %s, numero_ejemplares = %s, "
                               "id_materia = %s, id_curso = %s WHERE isbn = %s",
                               (self.titulo, self.autor, self.numero_ejemplares, self.id_materia, self.id_curso, self.isbn))
             conexion.commit()
             cursor.close()
             desconectar(conexion)
             print("Libro modificado correctamente")



