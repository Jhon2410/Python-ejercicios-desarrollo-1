"""
Una empresa tiene dos turnos (mañana y tarde) en los que
trabajan 8 empleados (4 por la mañana y 4 por la tarde)
Confeccionar un programa que permita almacenar los sueldos
de los empleados agrupados en dos listas. Imprimir las dos listas
de sueldos.
"""

sueldo_empleados = []
sueldo_empleados_maniana = []
sueldo_empleados_tarde = []
cantidad_empleados_maniana=cantidad_empleados_tarde = 4
acumulado_total=acumulado_maniana=acumulado_tarde= 0


for i in range(cantidad_empleados_maniana):
    sueldo = float(input(f"Digite el sueldo del empleado {i+1} jornada mañana : "))
    sueldo_empleados.append(sueldo)
    sueldo_empleados_maniana.append(sueldo)
    acumulado_total+=sueldo
    acumulado_maniana+=sueldo
for i in range(cantidad_empleados_maniana):
    sueldo = float(input(f"Digite el sueldo del empleado {i+1} jornada tarde : "))
    sueldo_empleados.append(sueldo)
    sueldo_empleados_tarde.append(sueldo)
    acumulado_total+=sueldo
    acumulado_tarde+=sueldo


print(f"\nTotal sueldos : {sueldo_empleados}\nPromedio total : {acumulado_total/len(sueldo_empleados)} ")
print(f"\nSueldos mañana : {sueldo_empleados_maniana}\nPromedio mañana : {acumulado_maniana/len(sueldo_empleados_maniana)} ")
print(f"\nSueldos  tarde : {sueldo_empleados_tarde}\nPromedio tarde : {acumulado_tarde/len(sueldo_empleados_tarde)} ")