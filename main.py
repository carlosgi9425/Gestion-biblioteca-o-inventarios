# Impor los módulos
import os 
from tabulate import tabulate
from conexion import *
from libro import *

#Importa la conexión
con = conectar()

# Inicia el menú
def iniciar():
    os.system("cls")
    while True:
        print("Seleccione una de las opciones: ")
        print("\t1 Añadir un libro")
        print("\t2 Ver todos los libros")
        print("\t3 Buscar un libro")
        print("\t4 Modificar un libro")
        print("\t5 Eliminar un libro")
        print("\t6 Salir")
        opcion = input ("Escoja una opcion: ")
        if opcion == "1":
            nuevo_libro()
        elif opcion =="2":
            ver_libros()
        elif opcion == "3":
            buscar_libro()
        elif opcion == "4":
            modificar_libro()
        elif opcion == "5":
            eliminar_libro()
        elif opcion == "6":
            break
        else:
            print(" Escoja una opción correcta")
        

# Permite agregar un nuevo libro
def nuevo_libro():
    titulo = input("Ingrese el titulo del libro: ")
    autor = input("Ingrese el nombre del autor: ")
    estado = "Disponible"
    respuesta = registar(titulo, autor, estado)
    print(respuesta)
 
# Muestra los libros   
def ver_libros():
    datos = mostrar()
    headers = ["ID", "TITULO", "AUTOR", "ESTADO"]
    tabla = tabulate(datos, headers, tablefmt="fancy_grid")
    print(tabla)
 
# Busca un libro por su ID 
def buscar_libro():
    id = input("Ingrese el ID del libro: ")
    datos = buscar(id)
    headers = ["ID", "TITULO", "AUTOR", "ESTADO"]
    tabla = tabulate(datos, headers, tablefmt="fancy_grid")
    print(tabla)

# Permite moficvar un libro por su ID
def modificar_libro():
    id = input("Ingrese el ID del libro a modficar: ")
    nuevo_valor= ""
    respuesta = ""
    campo = input("Selecione el campo que desea modificar\n1. Ttitulo\n2 Autor\n3 Estado\n")
    if campo == "1":
        nuevo_valor = input("Ingrese el nuevo Titulo del libro")
    elif campo == "2":
        nuevo_valor = input("Ingrese el nuevo Autor del libro")
    elif campo == "3":
        nuevo_valor = input("Ingrese el nuevo Estado del libro")    
    respuesta = modificar(id, campo, nuevo_valor)
    print(respuesta)

# Elimina un libro 
def eliminar_libro():
        id = input("Ingrese el ID del libro a eliminar: ")
        respuesta = eliminar(id)
        print(respuesta)
        
iniciar()