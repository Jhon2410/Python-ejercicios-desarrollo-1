"""
Almacenar en una lista los sueldos (valores float) de 5 operarios.
Imprimir la lista y el promedio de sueldos.
"""
operarios = []
cantidad_operarios = 5
promedio = 0
acumulado = 0
for i in range(cantidad_operarios):
    sueldo = float(input(f"Digite el sueldo del operario {i+1} : "))
    acumulado+=sueldo
    operarios.append(sueldo)

promedio = acumulado / cantidad_operarios

print(f"Operarios : {operarios}\nPromedio sueldo : {promedio} ")