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
                
        
def obtenerPerson(matriz_usuarios, lista_peliculas):
    numero_usuario = 1
    lista = []
    listaPelicula = []
    lista2 = []
    resultados = []
    for usuario in matriz_usuarios:
        if(usuario[0] == numero_usuario):
            lista.append(usuario[2])
            listaPelicula.append(usuario[1])
        else:
            for pelicula in lista_peliculas:
                for l in listaPelicula:
                    if(l == pelicula[0]):
                        lista2.append(pelicula[1])
            coeficiente = correlacionPearson(lista, lista2)
            resultados.append([usuario[0], coeficiente])
            numero_usuario = usuario[0]
            lista = []
            listaPelicula = []
            lista2 = []
            lista.append(usuario[2])
            listaPelicula.append(usuario[1])
        
    escribirCSV(resultados)
          

def escribirCSV(data):
    with open('./../data/person.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerows(data)

def main(): 
    seed(123456)

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

    
    obtenerPerson(matriz_usuarios,valoracionUsuario)

main()