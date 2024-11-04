# MAIN : Logica principal ABML (CRUD) create, read, update, delete. 
# Autor: Martin Maccorin
# Fecha: Octubre 2024
# 
# importa los codigos de colores.
from Colores import colores
# importa las funciones principales
from Funciones import agregar,mostrar
from Menu import Imprimir_Menu
opcion="0"
array_cod_prod=[]
array_desc_prod=[]
array_cant_prod=[]

while opcion != "5":
    Imprimir_Menu()

    opcion = str (input("ingrese una opcion: ")) 
    while opcion !='1'  and opcion !='2'  and opcion !='3' and opcion !='4'  and opcion !='5' :
        print("Caracter u Opcion no valida")
        opcion = str (input("ingrese un opcion: "))
        
    opcion = str(opcion) 
    if opcion == "1":
       array_cod_prod,array_desc_prod,array_cant_prod = agregar()
    elif opcion == "2":
        print(f"Elegiste la opcion: " + f"{opcion}")
    elif opcion == "3":
        print(f"Elegiste la opcion: " + f"{opcion}")
    elif opcion == "4":
        mostrar(array_cod_prod,array_desc_prod,array_cant_prod)
    elif opcion == "5":
        print(f"Elegiste la opcion: " + f"{opcion}" + "  --> ADIOS AMIGO!!!")
    