"""
Desarrollar un algoritmo que almacene N Clientes y los productos a comprar. Deben aplicar listas paralelas y:
Mostrar la lista general de los Clientes con sus productos.
Mostrar la factura de mayor venta y menor venta, promedio de venta por día de las facturas vendidas
Mostrar de manera ordena la lista de clientes con sus facturas.
Mostrar por cualquier método de eliminación de los clientes con facturas <= a 30000.
De acuerdo al requerimiento, aplicar las listas determinadas (Clientes y Producto
en componenentes de tipo lista.
"""

nombres_clientes = []
totales_clientes = []
Facturas = []
Cantidad = 0
acumulado_Total = 0
while Cantidad <= 0:
    Cantidad = int(input("Digite la cantidad de clientes a agregar : "))


for i in range(Cantidad):
    nombre = input(f"Digite el nombre del cliente {i+1} : ")
    nombres_clientes.append(nombre)
    seguir = True
    contador = 1
    Cliente = []
    nombres_productos = []
    valores_producto = []
    acumulado = 0
    while seguir:
        nombre_producto = input(f"Digite el nombre del producto {contador} del cliente {nombre} : ")
        valor_producto = int(input(f"Digite el valor del producto {nombre_producto} del cliente {nombre} : "))
        nombres_productos.append(nombre_producto)
        valores_producto.append(valor_producto)
        acumulado = acumulado + valor_producto
        if int(input("¿Desea agregar otro producto?\n1.si\n2.no\nRespuesta:")) == 2:
            seguir = False
            
        contador=contador + 1
    totales_clientes.append(acumulado)
    acumulado_Total = acumulado_Total + acumulado
    Cliente.append(nombres_productos)
    Cliente.append(valores_producto)
    Facturas.append(Cliente)
   

def burbuja(arreglo,arr2):
    longitud = len(arreglo)
    arreglo2=[]
    for i in range(longitud):
       for indice_actual in range(longitud - 1):
            indice_siguiente_elemento = indice_actual + 1
            if arreglo[indice_actual] > arreglo[indice_siguiente_elemento]:
                arreglo[indice_siguiente_elemento], arreglo[indice_actual] = arreglo[indice_actual], arreglo[indice_siguiente_elemento]
                arreglo2.append(nombres_clientes[indice_siguiente_elemento])
                arr2[indice_siguiente_elemento], arr2[indice_actual] = arr2[indice_actual], arr2[indice_siguiente_elemento]
                arr2.append(nombres_clientes[indice_siguiente_elemento])
           
            else:
                arreglo2.append(nombres_clientes[indice_actual])
    return arreglo,arr2

for i in range(len(nombres_clientes)):
    print(f"-----Factura {i+1}-----")
    print(f"cliente {nombres_clientes[i]}\n ")
    for j in range(len(Facturas[i][0])):
        print("-----Productos-----")
        print(f"{Facturas[i][0][j]} ---- ${Facturas[i][1][j]}")
    print(f"Total ---- ${totales_clientes[i]}")
    
ord1,ord2 = burbuja(totales_clientes,nombres_clientes)

print("--------------")
print(f"Mayor factura : ${ord1[-1]}\nMenor factura ${ord1[0]} \nPromedio : ${acumulado_Total / Cantidad}")

for i in range(len(ord1)):
    print("--Facturas ordenadas--")
    print(f"{ord1[i]} - {ord2[i]}")
    
print(f"{ord1} {ord2}")
        
                                                              
                                                              
   
        


    
    

