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
from person import correlacionPearson
import numpy as np
import csv

def nFilasAleatorias(n, csv_file ):
    filas = [[None for c in range(2)] for f in range(n)]
    with open(csv_file) as csv_file_movies:
        peliculas = list(csv.reader(csv_file_movies, delimiter=','))

    for i in range(n):
        indice = randint(1, 9742)
        filas[i][0] = int(peliculas[indice][0])
        filas[i][1] = peliculas[indice][1]

    return sorted(filas)

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
                
        
# def obtenerPerson(matriz_usuarios, lista_peliculas):
#     numero_usuario = matriz_usuarios[0][0]
#     lista = []
#     listaPelicula = []
#     lista2 = []
#     resultados = []
#     for usuario in matriz_usuarios:
#         if(usuario[0] == numero_usuario):
#             print("número de usuario",usuario[0])
#             lista.append(usuario[2])
#             listaPelicula.append(usuario[1])
#         else:
#             print("listaPelicula con la que compara" , listaPelicula)
#             for pelicula in lista_peliculas:
#                 print("tamaño listaPelicula: ", listaPelicula)
#                 for l in listaPelicula:
#                     print("lista comparacion",l)
#                     if(l == pelicula[0]):
#                         lista2.append(pelicula[1])
#             	#print("películaID",pelicula[0])
#                 #print("tamaño listaPelicula: ",listaPelicula)

#             	#for l in listaPelicula:
#                 #    print("lista comparación", l)
#                 #    if(l == pelicula[0]):
#                 #        lista2.append(pelicula[1])
            
#             print("Usuario ", usuario[0], ",",usuario[1],",",usuario[2])
#             print("Lista2 ", lista2)
#             print("Lista1 ", lista)
#             print("ListaPelicula: ", listaPelicula)
#             coeficiente = correlacionPearson(lista, lista2)
#             resultados.append([usuario[0], coeficiente])
#             numero_usuario = usuario[0]
#             lista = []
#             listaPelicula = []
#             lista2 = []
#             lista.append(usuario[2])
#             listaPelicula.append(usuario[1])
#             for l in lista_peliculas:
#                 if( l == listaPelicula[0]):
#                     lista2.append(l[1])
            
        
#     escribirCSV(resultados)


######################################################################################
#                                                                                    #
#   Usuario: matriz que continene en cada fila (idUsuario, idPelícula, Valoración)   #
#                                                                                    #
#   lista_peliculas: matriz que contiene (idPelicula, Valoración) del nuevo usuario. #
#                                                                                    #
######################################################################################
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

    escribirCSV(resultado)



def escribirCSV(data):
    with open('./../data/pearson.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerows(data)

def main(): 
    seed(12345)

    peliculas = nFilasAleatorias(20,"./../data/movies.csv")   
    matriz_usuarios = leerCSV("./../data/ratings.csv", peliculas)
    valoracionUsuario = [[None for c in range(2)] for f in range(20)]
    
    for i in range(len(peliculas)):
        valido = False
        while(not valido):
            valoracion = input("Valore la película " + peliculas[i][1] + " (0.0-5.0)\n")
            valoracion = float(valoracion)
            if(valoracion >= 0 and valoracion <= 5):
                valido = True
        valoracionUsuario[i][0] = peliculas[i][0]
        valoracionUsuario[i][1] = valoracion

    
    obtenerPearson(matriz_usuarios,valoracionUsuario)

main()
