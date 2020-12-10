###############################################################################
#                                                                             #
#                         GESTIÓN DE RECURSOS DIGITALES                       #
#                        UNIVERSIDAD DE GRANADA  (20/21)                      #
#                                                                             #
# Realizado por:                                                              #
#    -Bartolomé Zambrana                                                      #
#    -Pablo García López                                                      #
#    -Antonio Priego Raya                                                     #
#                                                                             #
###############################################################################

from random import seed
from random import randint
import numpy as np
import csv

def nFilasAleatorias(n, csv_file ):
    filas = [[None for c in range(2)] for f in range(n)]
    seed(123456)
    print(csv_file)
    with open(csv_file) as csv_file_movies:
        peliculas = list(csv.reader(csv_file_movies, delimiter=','))

    for i in range(n):
        indice = randint(1, 9742)
        filas[i][0] = peliculas[indice][0]
        filas[i][1] = peliculas[indice][1]

    return filas

#def leerCSV(csv_file):
    #wiht open(csv)
    



#def guardarCSV(nombre, directorio):
    

def main():
    nFilasAleatorias(20,"./Data/movies.csv")



main()