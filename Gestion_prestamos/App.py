from clases.curso import Curso
from clases.materia import Materia
from clases.libro import Libros
from clases.alumno import Alumno
from clases.prestamo import Prestamo

#curso = Curso("1A", "1ºESO")
#curso.insertar_curso()

#curso = Curso("2A", "2º ESO")
#curso.insertar_curso()

#materia = Materia("Lengua Castellana y Literatura", "Lengua")
#materia.insertar_materia()

#materia = Materia("Matematicas", "Matematicas")
#materia.insertar_materia()

#libro1 = Libros("978-84-670-5070-3", "Lengua Castellana 1º ESO", "Anaya", 10, 4, "1A")
#libro1.insertar_libro()

#libro2 = Libros("108-64-800-5020-9", "Matematicas 2º ESO", "Santillana", 20, 5, "2A")
#libro2.insertar_libro()

#libros = libro1.obtener_todos_libros()
#print("Todos los libros: ", libros)

#libro = libro1.obtener_un_libro("978-84-670-5070-3")
#print("Libro encontrado:", libro)


#libro3 = Libros("978-84-670-5070-3", "Lengua Castellana Modificado", "Anaya", 15, 4, "1A")
#libro3.modificar_libro()
#print("Libro modificado:", libro3.obtener_un_libro("978-84-670-5070-3"))

#alumno1 = Alumno("12345678A", "Juan", "Garcia Lopez", "I", True)
#alumno1.insertar_alumno()

#alumno2 = Alumno("23456789B", "María", "Parra herradura", "II", False)
#alumno2.insertar_alumno()

#alumnos = alumno1.obtener_todos_alumnos()
#print("Todos los alumnos: ", alumnos)

#alumno = alumno1.obtener_un_alumno("12345678A")
#print("Alumno encontrado: ", alumno)

#alumno3 = Alumno("12345678A", "Juan Modificado", "García López", "II", False)
#alumno3.modificar_alumno()
#print("Alumno modificado:", alumno3.obtener_un_alumno("12345678A"))

#prestamo = Prestamo("12345678A", "1A", "978-84-670-5070-3", "2024-09-10", "2025-06-20", "P")
#prestamo.asignar_prestamo()

#prestamos = prestamo.obtener_todos_prestamos()
#print("Todos los prestamos:", prestamos)

#prestamos_alumno = prestamo.obtener_por_alumno("12345678A")
#print("Prestamos del alumno:", prestamos_alumno)

#contrato = prestamo.generar_contrato("12345678A")
#print("Contrato:", contrato)

#prestamo.cerrar_prestamo("12345678A", "978-84-670-5070-3")
#print("Prestamo cerrado:", prestamo.obtener_por_alumno("12345678A"))