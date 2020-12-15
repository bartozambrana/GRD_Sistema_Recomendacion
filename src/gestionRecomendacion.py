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
from aux_funcs import *

######################################################################################
#   Para hallar los usuarios con mejores coeficientes de Person.                     #
#   Devuelve lista de 5 mejores vecinos                                              #
#                                                                                    #
#   list_person: lista de coeficientes de person necesaria para encontrar vecinos    # 
######################################################################################
def busquedaVecinos(list_person):
    vecinos=[ ["0","0"] , ["0","0"] , ["0","0"] , ["0","0"] ,["0","0"] ]
    for usuario in list_person:
        
        if abs( float(usuario[1]) ) > abs( float(vecinos[0][1]) ):
            vecinos[0] = usuario
            vecinos.sort(key=orden) # Mantiene vecinos siempre ordenado:
                                    # por lo que vecinos[0] es el que
                                    # menor person tiene de la lista

    lista_id_vecinos=[] #Lista final que contiene solamente los ID (int) de los vecinos
    for vecino in vecinos:
        lista_id_vecinos.append( int(vecino[0]) )

    return lista_id_vecinos


######################################################################################
#   Para hallar las peliculas con valoraciones aptas de vecinos.                     #
#   Devuelve lista de películas aptas                                                #
#                                                                                    #
#   id_peliculas_vistas: lista de IDs de peliculas que el usuario ya ha visto        # 
#   list_person: lista de coeficientes de person necesaria para encontrar vecinos    #
######################################################################################
def recomiendaPeliculas(id_peliculas_vistas, list_person):
    with open('./../data/ratings.csv', 'r') as csv_ratings:
        list_ratings = list(csv.reader(csv_ratings, delimiter=','))

    list_ratings.pop(0) #Eliminar cabecera

    peliculas_recomendadas    = []
    id_peliculas_recomendadas = []
    id_vecinos                = busquedaVecinos(list_person)

    for rating in list_ratings:
        for id_vecino in id_vecinos:
            if id_vecino == int(rating[0]):
                if float( rating[2] ) >= 4.5:
                    if (int(rating[1]) not in id_peliculas_vistas):
                        id_peliculas_recomendadas.append( int(rating[1]) )

    for id_pelicula in id_peliculas_recomendadas:
        peliculas_recomendadas.append( busqueda_binaria(id_pelicula) )


    return peliculas_recomendadas