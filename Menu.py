# MENU principal, se dibuja en pantalla las opciones del ABML (CRUD) create, read, update, delete.
# Autor: Martin Maccorin
# Fecha: Octubre 2024
#
# importa los codigos de colores.
from Colores import colores
# importa las funciones principales
from Funciones import agregar,mostrar

def Imprimir_Menu():
    # define variables de para el uso de colores.
    amarillo, azul, blanco, rojo, cian, verde = colores()

    # define variables de para el uso de espacios.
    sangria = int(15)
    # defino variables por cada renglon a mostrar.
    letra_blanco = f"{blanco}"+" "
    factor = int(60)
    factor_der = int(15)
    factor_izq_menu = int(sangria + 3)
    factor_izq = int(sangria)


    # variables para calculo de encolumnamiento.
    renglon_asteriscos = f"{azul}" + factor * "*"

    # calcula la posicion del ultimo asterisco (-2 es por los 2 asteriscos)

    # linea vacia con marco de asterisco
    renglon_vacio = factor_izq * " "
    factor_der_vacio = factor - len(renglon_vacio) - factor_izq - 2
    color_espacio_der_vacio = + factor_der_vacio * " " + f"{azul}"+"*"

    # linea del menu principal
    espacio_izq_menu = factor_izq_menu * " "
    asterisco = "*"
    color_espacio_izq_menu = f"{azul}" + \
    f"{asterisco}"+f"{espacio_izq_menu}" + f"{verde}"

    linea_menu = "MENU PRINCIPAL"
    color_espacio_izq = f"{azul}"+"*"+factor_izq * " "+f"{amarillo}"
    factor_der = factor - len(linea_menu) - factor_izq_menu - 2
    color_espacio_der = + factor_der * " " + f"{azul}"+"*"

    # Linea 1 del menu.
    linea_1 = "1. Ingresar producto"
    factor_der1 = factor - len(linea_1) - factor_izq - 2
    color_espacio_der1 = + factor_der1 * " " + f"{azul}"+"*"

    # Linea 2 del menu.
    linea_2 = "2. Modificar producto"
    factor_der2 = factor - len(linea_2) - factor_izq - 2
    color_espacio_der2 = + factor_der2 * " " + f"{azul}"+"*"

    # Linea 3 del menu.
    linea_3 = "3. Borrar producto"
    factor_der3 = factor - len(linea_3) - factor_izq - 2
    color_espacio_der3 = + factor_der3 * " " + f"{azul}"+"*"

    # Linea 4 del menu.
    linea_4 = "4. Listado de productos"
    factor_der4 = factor - len(linea_4) - factor_izq - 2
    color_espacio_der4 = + factor_der4 * " " + f"{azul}"+"*"

    # Linea 5 del menu.
    color_rojo_espacio_izq = f"{azul}"+"*"+factor_izq * " "+f"{rojo}"
    linea_5 = "5. Salir"
    factor_der5 = factor - len(linea_5) - factor_izq - 2
    color_espacio_der5 = + factor_der5 * " " + f"{azul}"+"*"


    # impresion del menu por pantalla.
    # pongo letra en blanco
    print(f"{letra_blanco}")
    # pongo marco en color
    print(f"{renglon_asteriscos}")
    print(f"{color_espacio_izq_menu}" + linea_menu + color_espacio_der)
    # pongo marco en color
    print(f"{renglon_asteriscos}")
    print(f"{color_espacio_izq}" + renglon_vacio + color_espacio_der_vacio)
    print(f"{color_espacio_izq}" + linea_1 + color_espacio_der1)
    print(f"{color_espacio_izq}" + linea_2 + color_espacio_der2)
    print(f"{color_espacio_izq}" + linea_3 + color_espacio_der3)
    print(f"{color_espacio_izq}" + linea_4 + color_espacio_der4)
    print(f"{color_espacio_izq}" + renglon_vacio + color_espacio_der_vacio)
    print(f"{color_rojo_espacio_izq}" + linea_5 + color_espacio_der5)
    print(f"{color_espacio_izq}" + renglon_vacio + color_espacio_der_vacio)
    # pongo marco en color
    print(f"{renglon_asteriscos}")
    # pongo letra en blanco
    print(f"{letra_blanco}")