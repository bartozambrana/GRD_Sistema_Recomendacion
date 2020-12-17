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

from gestionRecomendacion import recomiendaPeliculas
from pearson import obtenerPearson
from gestionCSV import nFilasAleatorias
from gestionCSV import leerCSV


def main():
    peliculas = nFilasAleatorias(20,"./../data/movies.csv")   
    matriz_usuarios = leerCSV("./../data/ratings.csv", peliculas)
    valoracionUsuario = [[None for c in range(2)] for f in range(20)]
    id_peliculas_vistas = []
    
    for i in range(len(peliculas)):
        valido = False
        while(not valido):
            valoracion = input("Valore la película " + peliculas[i][1] + " (0.0-5.0)\n")
            valoracion = float(valoracion)
            if(valoracion >= 0 and valoracion <= 5):
                valido = True
        valoracionUsuario[i][0] = peliculas[i][0]
        id_peliculas_vistas.append(int(peliculas[i][0]))
        valoracionUsuario[i][1] = valoracion

    
    coeficientes_pearson = obtenerPearson(matriz_usuarios,valoracionUsuario)
    
    recomendadas = set (recomiendaPeliculas(id_peliculas_vistas, coeficientes_pearson)) 
    
    
    print("\t  ---------------------- \t \t")
    print("\t  PELICULAS RECOMENDADAS \t \t")
    print("\t  ---------------------- \t \t\n")

    for pelicula in recomendadas :
        print("\t -> ",pelicula)

main()