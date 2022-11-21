#Cargar n cantidad de componentes listas que simulen a un estudiante con nombre, edad y nota.
#dentro de una lista salon

salon = []
seguir = True
contador=1
acumulado=0
lista_nombre=[]
lista_edad=[]
lista_nota=[]
while seguir:
    estudiante = []
    nombre = input(f"Digite el nombre del estudiante   {contador} :")
    edad = input(f"Digite la edad del estudiante   {contador} :")
    nota = float(input(f"Digite la nota del estudiante   {contador} :"))
    lista_nombre.append(nombre)
    lista_edad.append(edad)
    lista_nota.append(nota)
    estudiante.append(nombre)  
    estudiante.append(edad)    
    estudiante.append(nota) 
    salon.append(estudiante)
    acumulado+=nota
    opcion = int(input("Desea seguir ? \n1.si\n2.no \nRes: "))
    if opcion == 2:
        seguir = False

promedio = acumulado / len(salon)
print(f"Componentes listas : {salon} \nListas paralelas : \nNombres : {lista_nombre}\nEdades : {lista_edad}\nNotas : {lista_nota}\nCon un promedio acumulado de : {promedio}")
    

        
