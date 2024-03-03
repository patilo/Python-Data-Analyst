import pandas as pd

def filtrar_por_fechas(dataframe, columna_fecha, fecha_inicio, fecha_fin):
    return dataframe[(dataframe[columna_fecha] >= fecha_inicio) & (dataframe[columna_fecha] <= fecha_fin)]

def generar_reporte_pivot(dataframe, filas, columnas, valores, funcion_agrupadora):
    pivote = pd.pivot_table(dataframe, index=filas, columns=columnas, values=valores, aggfunc=funcion_agrupadora, fill_value=0)
    return pivote

def escribir_en_postgres(dataframe, nombre_tabla, engine, if_exists):
    dataframe.to_sql(nombre_tabla, engine, if_exists=if_exists, index=False)

