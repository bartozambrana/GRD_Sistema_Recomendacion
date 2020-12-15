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

import math
from gestionCSV import escribirCSV



######################################################################################
#   x: lista sobre la que hay que obtener la media                                   #  
#   Devulve la media de la lista dada                                                #
######################################################################################
def media(x):
    assert len(x) > 0
    
    return sum(x)/len(x)

######################################################################################
#   x: lista 1 para obtener el coeficiente de correlación                            #
#   y: lista 2 para obtener el coeficiente de correlación                            #
#   Devuelve un float con el coeficiente de corrrelación de pearson                  #
######################################################################################
def correlacionPearson(x,y):
    assert len(x) == len(y)

    mediaX = media(x)
    mediaY = media(y)

    normalizaX = 0
    normalizaY = 0

    numerador = 0
    
    for i in range(len(x)):
        diffX = ( x[i]- mediaX )
        diffY = ( y[i] - mediaY )
        numerador += (diffX * diffY)
        normalizaX += (diffX * diffX)
        normalizaY += (diffY * diffY)
        
    denominador = (math.sqrt(normalizaX) * math.sqrt(normalizaY))
    
    if denominador == 0 :
        denominador = 1 #Da igual, si vale 0 es porque x o y ha puntuado todas igual, por lo tanto el numerador vale 0

    return numerador/denominador

#######################################################################################
#   usuario: matriz que continene en cada fila (idUsuario, idPelícula, Valoración)    #                                                                                    #
#   lista_peliculas: matriz que contiene (idPelicula, Valoración) del nuevo usuario.  #
#   Devuelve una matriz con los coeficientes dado a las valoraciones de un usuario    #
#   en formato de cada fila(idUsario, coeficiente)                                    #
#   Escribe dicho resultado también en un fichero llamado pearson.csv, ubicado en data#
#######################################################################################
def obtenerPearson(usuarios, lista_peliculas):
    
    #   VARIABLES NECESARIAS: seguimos la estrategia de un usuario anterior y el usuario actual.

    usuario_anterior = usuarios[0][0] #usuario anterior.
    lista_valoraciones = []           #lista de valoraciones para un usuario x de los registrados.
    lista_peliculas_valoradas = []    #lista de idPelículas a las que ha valorado el usuario x
    lista_valoraciones_usuario = []   #lista de valores del usuario del sistema, para las películas comunes.
    resultado = []

    lista_valoraciones.append(usuarios[0][2])
    lista_peliculas_valoradas.append(usuarios[0][1])

    #veamoslo para todos los usuarios, teniendo en cuanta el usuario anterior. Obteniendo el coeficiente cuando cambiemos de usuario.
    for i in range(1,len(usuarios)):
        if usuario_anterior == usuarios[i][0] : #comparamos el usuario anterior con el actual.
            lista_valoraciones.append(usuarios[i][2])
            lista_peliculas_valoradas.append(usuarios[i][1]) 
        else : #usuario anterior distinto al actual, hay que volcar los datos, y tomar los datos de la fila actual, obteniendo la intersección de los elmentos del usuario.
            for pelicula in lista_peliculas :
                if pelicula[0] in lista_peliculas_valoradas :
                    lista_valoraciones_usuario.append(pelicula[1])
            
            #obtenemos el coeficiente de pearson.
            coeficiente = correlacionPearson(lista_valoraciones, lista_valoraciones_usuario)
            resultado.append([usuarios[i][0],coeficiente])
            
            #limpiamos lista de valores.
            lista_valoraciones = [] 
            lista_valoraciones_usuario = []
            lista_peliculas_valoradas = []

            #Añadimos los valores de la fila actual.
            usuario_anterior = usuarios[i][0]
            lista_valoraciones.append(usuarios[i][2])
            lista_peliculas_valoradas.append(usuarios[i][1])

    escribirCSV(resultado,'./../data/pearson.csv')
    return resultado