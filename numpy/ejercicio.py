#Ventas de Supermercado
#Imagina que tienes una matriz donde las filas son 3 tiendas y las columnas son 4 meses de ventas.

import numpy as np

# Ventas (Filas: Tiendas | Columnas: Meses)
ventas = np.array([
    [100, 120, 110, 150], # Tienda A
    [500, 50, 60, 70],    # Tienda B (El 500 es un outlier)
    [200, 210, 190, 205]  # Tienda C
])

# --- PROMEDIOS (MEAN) ---
# Promedio de ventas por MES (colapsa las filas)
promedio_mes = np.mean(ventas, axis=0) 
# Resultado: [266.6, 126.6, 120.0, 141.6]

# Promedio de ventas por TIENDA (colapsa las columnas)
promedio_tienda = np.mean(ventas, axis=1)
# Resultado: [120.0, 170.0, 201.2]

# --- MEDIANA (MEDIAN) ---
# Muy útil para la Tienda B que tiene un 500 (valor muy alto)
mediana_tienda_b = np.median(ventas[1, :]) 
# Resultado: 65.0 (Mucho más realista que su promedio de 170)

# --- DESVIACIÓN ESTÁNDAR (STD) ---
# ¿Qué tienda es más "estable" en sus ventas?
estabilidad = np.std(ventas, axis=1)
# La Tienda C tendrá un número bajo (ventas parecidas: 190, 200, 210)
# La Tienda B tendrá un número altísimo (por el salto de 500 a 50)