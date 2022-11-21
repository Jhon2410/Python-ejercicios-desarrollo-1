#                   TALLER CD CON PYTHON

#1. Compilar el source y corregir.
#2. Documentar el source. (describir la funcionalidad del source por línea)
#3. Documenta el Test Report
#4. Aplicar dos Listas en un Diccionario y mostrar el Diccionario en un DataFrame


import pandas as pd # se importa panda
import numpy as np # se importa numpy
def defdatos(a,b,c): # se define la funcion defdatos
    labels = ["a","b","c"] # se crea unalista llamada labels
    my_list = [a,b,c] # se crea una lista con unos valores que viene como arguemntos de la funcion defdatos
    arr = np.array([a,b,c]) # se crea un array usando numpy 
    dicc = {"a":a,"b":b,"c":c} # se crea un dicionario
    print("") # salto de linea
    print(pd.Series(my_list, labels)) # se imprime una serie
    print(type(my_list)) # se imprime de que tipo es la lista 
    print("") # salto de linea
    print(pd.Series(arr,labels)) # se crea una serie con el arreglo y los labels
    print(type(arr)) # se imprime de que tipo de dato es el arreglo
    print("") # salto de linea
    print(pd.Series(dicc)) # se crea un serie con el diccionario
    print(type(dicc)) # se imprime el tipo de dato del label
n1=input("digite valor num1: ") # se lee la variable n1
n2=input("digite valor num2: ") # se lee la variable n2
n3=input("digite valor num3:")  # se lee la variable n3
defdatos(n1,n2,n3)  # se lee la variable n1
print("") # salto de linea
#    print(os.getcwd()) # esto no se está usando pero solo es acceder al sistema 
#    print(os.listdir()) # esto no se está usando pero solo es acceder al sistema 
print("") # salto de linea
print("Nómina mensual CafeFull Colombia") # imprimir titulo
nomb1="rancisco Perez" # se lee la variable nomb1
nomb2="Amira Nieto"    # se lee la variable nomb2
nomb3="Juan Cataño"    # se lee la variable nomb3
datos = np.array([[1000000,1200000,1450000],[900000,1100000,1300000],[1300000,1400000,1500000]])  # se define una matriz con los salarios de tres empleados en tres meses
datosfinal= pd.DataFrame(datos,index=[nomb1,nomb2,nomb3],
columns=["Octubre","Noviembre","Diciembre"])  # se crea un dataframe
print(datosfinal)  # se imprime el dataframe
print("") # salto de linea

print("Nómina mensual CafeFull Colombia") # imprimir titulo
nomb1="Francisco Perez" # se lee la variable nomb1
nomb2="Amira Nieto"     # se lee la variable nomb2
nomb3="Juan Cataño"     # se lee la variable nomb3
#nomb4= "Juanita Mora"
datos = [[1000000,1200000,1450000],[900000,1100000,1300000],[1300000,1400000,1500000]] # se define una matriz con los salarios de tres empleados en tres meses
datosfinal= pd.DataFrame(datos,index=[nomb1,nomb2,nomb3],
columns=["Octubre","Noviembre","Diciembre"]) # se crea un dataframe
print(datosfinal) # se imprime el dataframe

#Aplicar dos Listas en un Diccionario y mostrar el Diccionario en un DataFrame

lista1 =["carro","moto","bicicleta"]
lista2 =[1,2,25]
#print(pd.Series(lista2,lista1))

if len(lista1) == 0 and len(lista2) == 0:
    print("Las listas están vacias.")
else:
    print("-"*len("dicionario a data frame"))
    print("dicionario a data frame")
    print("-"*len("dicionario a data frame"))
    dicionario = {
           "vehiculos": lista1,
           "Personas_cantidad" : lista2
        }
    
    print(pd.DataFrame(dicionario))






