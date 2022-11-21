# Definir una lista que almacene 5 enteros. Sumar todos sus elementos (ciclo) y
# mostrar los elementos de la lista y dicha suma.

Lista=[2,4,6,8,10]
sumatoria = 0
x=0
while x < len(Lista):
    sumatoria+=Lista[x]
    x=x+1
print(f"El resultado de la sumatoria de {len(Lista)} Numeros es :{sumatoria}")

