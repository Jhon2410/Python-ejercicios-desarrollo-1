# Definir una lista por asignación con 5 enteros. Mostrar por pantalla (ciclo) solo
# los elementos con valor iguales o superiores a 7.

# Definir variables 
lista_inicial=[]
lista_numeros_mayores=[]
lista_numeros_menores=[]
limite=7
cantidad_numeros=5



def leer_numeros():
    for i in range(cantidad_numeros):
        lista_inicial.append(int(input(f"Digite el numero {i+1} :")))
    calcular_mayores()

def calcular_mayores():
    for i in range(len(lista_inicial)):
        if lista_inicial[i] >= limite:
            lista_numeros_mayores.append(lista_inicial[i])
        else:
            lista_numeros_menores.append(lista_inicial[i])
    imprimir_resultado()
def imprimir_resultado():
    print(f"Lista inicial : {lista_inicial} \nLista de numeros mayores a {limite} : {lista_numeros_mayores} \nLista numeros menores a {limite} : {lista_numeros_menores}. ")

def start_app():
    leer_numeros()

start_app()