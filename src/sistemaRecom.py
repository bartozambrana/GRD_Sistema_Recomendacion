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

import csv


#Para hallar los usuarios con mejores coeficientes de Person.
#Devuelve lista de 5 mejores vecinos
def busquedaVecinos():

    usuarios_person_finales=[0,0,0,0,0]
    for indice in range(num_usuarios):
        usuario_person_actu = llamadaFunciónDeCompas(indice)
        
        if usuario_person_actu.person > usuario_person_finales[0]:
            usuarios_person_finales[0] = usuario_person_actu
            usuarios_person_finales.sort()

    return usuarios_person_finales


#Para hallar las peliculas con valoraciones aptas de vecinos
#Devuelve lista de películas aptas
def recomiendaPeliculas(vecino, lista_peliculas):
    peliculas_recomendadas = []

    for pelicula in lista_peliculas:
        if pelicula.rating >= 4.0:
            peliculas_recomendadas.append(pelicula)

    return peliculas_recomendadas




def main():
    print ("main de sistemaRecom")

main()