#Titulo              Ejercicio 2
#Descripcion         Convertir de grados centigrados a grados Farenheit
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
    print ("CONVERSOR CENTIGRADOS A FAHRENHEIT")
    print ("__________________________________")
    print()
    #Variable de entrada
    centigrados = input("Introduce el numero en centígrados (º) :")
    #
    try:
        #Operacion
        farenheit=(float(centigrados)*(9/5)+32)
        #
        #Mostrar resultado
        cls()
        print ("Visto lo visto, " + centigrados + "ºC equivale a " + str(farenheit) + "ºF")
        someError = 0
    #
    #Si la operacion no se puede llevar a cabo
    except ValueError:
        if ("," in centigrados):
            cls()
            print ("Los decimales van separados con un punto, no con una coma")
            someError += 1
            time.sleep(5)
        else:
            cls()
            print ("El valor introducido no es correcto")
            someError += 1
            time.sleep(5)