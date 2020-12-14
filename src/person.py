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

import math

def media(x):
    assert len(x) > 0
    return float(sum(x))/len(x)

#Asumiendo que x e y
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

