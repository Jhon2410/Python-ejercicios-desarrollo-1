"""
Cargar por teclado y almacenar en una lista las alturas de 5
personas (valores float)
Obtener el promedio de las mismas. Contar cuántas personas
"""
alturas_personas = []
cantidad_personas = 5
promedio = 0
acumulado = 0
for i in range(cantidad_personas):
    altura = float(input(f"Digite la altura de la persona {i+1} : "))
    acumulado+=altura
    alturas_personas.append(altura)

promedio = acumulado / cantidad_personas

print(f"cantidad de personas : {cantidad_personas}  \nAlturas  : {alturas_personas}\nPromedio alturas : {promedio} ")