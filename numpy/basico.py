#numpy es una libreria que nos permite trabajar con arrays de manera eficiente
#esta libreria la utilizaremos para trabajar con datos numericos y matematicos
#para ser mas claro la usamos en vectores y matrices
#para poder usar numpy debemos importarlo

import numpy as np

#creamos un array de numpy
array = np.array([1, 2, 3, 4, 5])
print(array)
#como podemos ver es una lista pero con numpy es mas eficiente y rapido
#ademas podemos hacer operaciones con los arrays de manera mas sencilla

#tambien podemos hacer sumas, restas, multiplicaciones, divisiones, etc
array = array + 2
array = array - 2
array = array / 2
array = array * 2
#podemos tambien usar funciones trigonometricas, logaritmos, etc
array = np.sin(array)
print(array)
array = np.cos(array)
print(array)
array = np.tan(array)
print(array)
array = np.sqrt(array)
print(array)
array = np.log(array)
print(array)
array = np.log10(array)
print(array)
array = np.log2(array)

#podemos crear arrays de ceros y unos
array = np.zeros(5)
#indicamos la cantidad de ceros que queremos
print(array)

#otra cosa que podemos hacer y mas intermedio, es crear matrices
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matriz)
#pero lo mas potente de numpy es que podemos hacer operaciones con las matrices de la misma manera que con los arrays
#usaremos la funcion reshape() y axis, calculo de la media, mediana, desviacion estandar, etc
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
np.mean(array) #media, es la suma de todos los elementos dividido por la cantidad de elementos
np.median(array) #mediana, es el valor que se encuentra en el medio del array
np.std(array) #desviacion estandar, la desviacion estandar es una medida de la dispersion de los datos
np.var(array) #varianza, la varianza es la desviacion estandar al cuadrado
























