#Titulo              Ejercicio 3
#Descripcion         Diagrama que diga si un numero es par o non.
#
#Importaciones
import os
import time
#
#
#Funciones - Borrar consola cls()
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
#
#
#Debug - Operacion
someError = 1
#
#Menu Loop
while someError > 0:
    #
    #Enseñar Menu
    cls()
    print ("COMPROBADOR DE NUMEROS PARES")
    print ("__________________________________")
    print()
    #Variable de entrada
    numeroIntroducido = input("Introduce un numero entero :")
    #
    try:
        #Operacion
        if int(numeroIntroducido)%2 == 0:
        #
            #Mostrar resultado
            cls()
            print ("El numero " + numeroIntroducido + " es par")
            someError = 0
        else:
            #Mostrar resultado
            cls()
            print ("El numero " + numeroIntroducido + " es impar")
            someError = 0
    #
    #Si la operacion no se puede llevar a cabo
    except ValueError:
        if ("," in numeroIntroducido or "." in numeroIntroducido):
            cls()
            print ("El numero no puede contener decimales")
            someError += 1
            time.sleep(5)
        else:
            cls()
            print ("El valor introducido no es correcto")
            someError += 1
            time.sleep(5)