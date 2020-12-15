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

import csv


######################################################################################
#   Función de criterio de ordenación.                                               #
#                                                                                    #
#   person: tupla presente en person.csv que se pretende ordenar                     #
######################################################################################
def orden(person):
    return abs( float(person[1]) )


######################################################################################
#   Busqueda binaria.                                                                #
#                                                                                    #
#   x: elemento que se busca                                                         #
######################################################################################
def busqueda_binaria(x):
    with open('./../data/movies.csv', 'r') as csv_movies:
        peliculas = list(csv.reader(csv_movies, delimiter=','))

    izq = 1
    der = len(peliculas) -1 

    while izq <= der:
        medio = int((izq+der)/2)
        
        if int(peliculas[medio][0]) == x :
            return peliculas[medio][1]

        elif int (peliculas[medio][0]) > x :
            der = medio-1
        else:
            izq = medio+1

    return -1
