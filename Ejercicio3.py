# Definir por asignación una lista con 8 elementos enteros. Contar (ciclo) cuantos
# de dichos valores almacenan un valor superior a 100. Mostrar los elementos de
# la lista y los valores superiores a 100.

# los elementos con valor iguales o superiores a 7.

# Definir variables 
lista_inicial=[]
lista_numeros_mayores=[]
lista_numeros_menores=[]
limite=100
cantidad_numeros=8



def leer_numeros():
    for i in range(cantidad_numeros):
        lista_inicial.append(int(input(f"Digite el numero {i+1} :")))
    calcular_mayores()

def calcular_mayores():
    for i in range(len(lista_inicial)):
        if lista_inicial[i] > limite:
            lista_numeros_mayores.append(lista_inicial[i])
        else:
            lista_numeros_menores.append(lista_inicial[i])
    imprimir_resultado()
def imprimir_resultado():
    print(f"Lista inicial : {lista_inicial} \nLista de numeros mayores a {limite} : {lista_numeros_mayores} \nLista numeros menores o igual {limite} : {lista_numeros_menores}. ")

def start_app():
    leer_numeros()

start_app()