"""
Definir una lista que almacene por asignación los nombres de 5 personas.
Contar (ciclo) cuantos de esos nombres tienen 5 o más caracteres.
Mostrar la lista de nombres y la cantidad de nombres con 5 o mas caracteres.
"""

numero_personas = 5
nombres_personas = []
nombres_igual_mayores_personas = []
nombres_menores_personas = []
cantidad_caracters = []
limite_caracteres = 5

for i in range(numero_personas):
    nombre = input(f"Digite el nombre de la personas {i+1} : ")
    nombres_personas.append(nombre)
    cantidad_caracters.append(len(nombre))
    if len(nombre) >= limite_caracteres:
        nombres_igual_mayores_personas.append(nombre)
    else:
        nombres_menores_personas.append(nombre)
        
            
print(f"\nNombres ingresados : {nombres_personas}\nCaracteres : {cantidad_caracters}\ncantidad {len(nombres_personas)}\nNombres personas con {limite_caracteres} o mas caracteres : \n{nombres_igual_mayores_personas}  \ncantidad : {len(nombres_igual_mayores_personas)}\nNombres personas con menos de {limite_caracteres} \ncatacteres : {nombres_menores_personas} \ncantidad : {len(nombres_menores_personas)}")
        