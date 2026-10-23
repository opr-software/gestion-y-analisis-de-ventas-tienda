import numpy as np

# Programa para gestionar las ventas durante 10 días.

#1. Crear identificadores para los días con np.arange(). (hecho)
#2. Crear arrays con las ventas utilizando np.array(). (hecho)
#3. Inicializar registros con np.zeros(). (hecho)
#4. Crear arrays de unos con np.ones(). (hecho)
#5. Realizar operaciones matemáticas entre arrays. (hecho)
#6. Calcular las ventas después de aplicar un descuento. (hecho)
#7. Crear una matriz de ventas de diferentes productos. (hecho)
#8. Simular una secuencia descendente. (hecho)
#9. Identificar los días con mejores resultados.

#Objetivo: combinar arrays, operaciones matemáticas, ceros, unos, secuencias y matrices en un único programa.

dias = np.arange(1, 11)
print("Días: ", dias)

registros = np.zeros(10)
print("Registros: ", registros)

descuentos = np.ones(10) * 0.8 # Descuentos para cada día.
print("Descuentos: ", descuentos)

ventas_10_días = np.arange(1000, 0, -100) * descuentos # Secuencia descendente
print("Ventas: ", ventas_10_días)

#crear matriz de ventas de diferentes productos
productos = np.array([[10, 203], [20,30], [30,40], [40,50], [50,60], [60,70], [70,80], [80,90], [90,100], [100,110]]) 
print("Productos: ", productos)

print("Mejor día:", ventas_10_días.max())