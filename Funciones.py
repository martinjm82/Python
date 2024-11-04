# Definicion de Funciones 
#defino una funcion agregar.. valida e ingresa los datos.
def agregar():
    codigo_producto=""
    descripcion_producto=""
    cantidad_producto=0

    array_cod_prod = []
    array_desc_prod= []
    array_cant_prod= []
 
    while codigo_producto.lower() !="x":
        print(60*"*")
        codigo_producto=str(input("ingrese el codigo del producto o x para terminar: "))
        print(60*"*")
        if  codigo_producto.lower() !="x": 
            descripcion_producto=str(input("ingresa la descripcion del producto: "))
            cantidad_producto=int(input(f"ingresa la cantidad de producto: "))
            array_cod_prod.append(codigo_producto)
            array_desc_prod.append(descripcion_producto)
            array_cant_prod.append(cantidad_producto)
    
    return array_cod_prod,array_desc_prod,array_cant_prod
    

def mostrar(array_cod_prod,array_desc_prod,array_cant_prod):
# Muestra los productos cargados.
    op=""
    while op.lower() !="x":
        long_codigo_producto=len(array_cod_prod)
        i=0
        print(60*"*")
        if long_codigo_producto == 0:
           print("No hay datos a mostrar") 
            

        while i < long_codigo_producto:
            print(f"Código de producto ", array_cod_prod[i] , " Descripcion: " , array_desc_prod[i] , 
            " cantidad: " , array_cant_prod[i])
            i+=1
        print(60*"*")
        op=str(input("Ingrese x para volver al menu: "))


