#Titulo              Ejercicio 4
#Descripcion         Diagrama para calcular el mayor de dos numeros.
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
    print ("CUAL ES EL MAYOR DE DOS NUMEROS")
    print ("________________________________")
    print()
    #Variables de entrada
    primerNumero = input("Introduce el primer numero :")
    segundoNumero = input("Introduce el segundo numero :")
    #
    #Intentar realizar operacion
    try:
        #Si el primer numero es mas grande
        if float(primerNumero) > float(segundoNumero):
            #
            #Mostrar resultado
            cls()
            print (str(primerNumero) + " es mayor que " + str(segundoNumero))
            someError = 0

        #Si el segundo numero es mas grande
        elif float(primerNumero) < float(segundoNumero):
            cls()
            print (str(primerNumero) + " es menor que " + str(segundoNumero))
            someError = 0
        else:
            cls()
            print ("Los numeros son iguales")
            someError = 0 
    #
    #Si la operacion no se puede llevar a cabo
    except ValueError:
        cls()
        print ("Algunos valores no son correctos")
        someError += 1
        time.sleep(5)