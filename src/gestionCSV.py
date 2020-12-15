######################################################################################
#                                                                                    #
#                         GESTIÓN DE RECURSOS DIGITALES                              #
#                        UNIVERSIDAD DE GRANADA  (20/21)                             #
#                                                                                    #
# Realizado por:                                                                     #
#    -Bartolomé Zambrana                                                             #
#    -Pablo García López                                                             #
#    -Antonio Priego Raya                                                            #
#                                                                                    #
######################################################################################

from random import seed
from random import randint
import numpy as np
import csv



######################################################################################
#   n: número de películas aleatorias a escoger                                      #
#   csv_file: documento csv a leer                                                   #
#   Devuelve una lista ordenada de identificadores de películas de manera aleatoria  #
######################################################################################
def nFilasAleatorias(n, csv_file ):
    seed(12345)
    filas = [[None for c in range(2)] for f in range(n)]
    with open(csv_file) as csv_file_movies:
        peliculas = list(csv.reader(csv_file_movies, delimiter=','))

    for i in range(n):
        indice = randint(1, 9742)
        filas[i][0] = int(peliculas[indice][0])
        filas[i][1] = peliculas[indice][1]

    return sorted(filas)


######################################################################################
#   Usuario: matriz que continene en cada fila (idUsuario, idPelícula, Valoración)   #                                                                                    #
#   lista_peliculas: matriz que contiene (idPelicula, Valoración) del nuevo usuario. #
#   Devuelve una matriz con los ratings, ya estableciendo los tipos entero           #
######################################################################################
def leerCSV(csv_file, lista_peliculas):
    with open(csv_file) as csv_file_movies:
        ratings = list(csv.reader(csv_file_movies, delimiter=','))
    
    resultado = [[None for c in range(3)] for f in range(len(ratings))]

    matriz = []
    ignorar = 0

    for rating in ratings:
        if(ignorar != 0):
            aux = []
            aux.append(int(rating[0])) 
            aux.append(int(rating[1]))
            aux.append(float(rating[2]))

            for pelicula in lista_peliculas:
                if(aux[1] == pelicula[0]):
                    matriz.append(aux)
        else:
           ignorar = ignorar + 1
 
    return matriz
                
######################################################################################
#   data: conjunto de datos a escribir.                                              #
#   ruta: ruta al fichero donde hay que escribirlo.                                  #
######################################################################################
def escribirCSV(data,ruta):
    with open(ruta, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerows(data)


