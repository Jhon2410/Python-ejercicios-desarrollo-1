"""
#Realizar la carga de valores enteros por teclado, almacenarlos en
una lista.
Finalizar la carga de enteros al ingresar el cero. Mostrar finalmente el
tamaño de la lista y la lista de elementos cargados.
"""

cerrar = 0
seguir = True
numeros_enteros = []

while seguir:
    numero = int(input(f"Digite el numero entero {len(numeros_enteros) + 1} :"))
    if numero == cerrar :
        seguir = False
    else:
        numeros_enteros.append(numero)
        
print(f"Números cargados :  {numeros_enteros}\nCantidad números cargados : {len(numeros_enteros)} ")
            