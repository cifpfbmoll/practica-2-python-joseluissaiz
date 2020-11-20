#Titulo              Ejercicio 1
#Descripcion         Hacer un diagrama de flujo para calcular y mostrar
#                    el area de un triangulo.
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
    print ("CALCULAR EL AREA DE UN TRIANGULO")
    print ("________________________________")
    print()
    #Variables de entrada
    base = input("Introduce la base del triangulo (en metros) :")
    altura = input("Introduce la altura del triangulo (en metros) :")
    #
    #Intentar realizar operacion
    try:
        #Operacion
        area=(float(base)*float(altura))/2
        #
        #Mostrar resultado
        cls()
        print ("El area es de " + str(area) + " metros")
        someError = 0
    #
    #Si la operacion no se puede llevar a cabo
    except ValueError:
        if ("," in base) or ("," in altura):
            cls()
            print ("Los decimales van separados con un punto, no con una coma")
            someError += 1
            time.sleep(5)
        else:
            cls()
            print ("Algunos valores no son correctos")
            someError += 1
            time.sleep(5)