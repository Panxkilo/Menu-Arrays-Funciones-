from os import system
from Package_Arrays.Array_Generales import *
from Package_Arrays.Especificas import *
from Package_Input.Funciones_Input import *
menu=True
numeros = []
while menu:
    opcion = input("a. Ingresar Numeros\nb. Mostrar cantidad de positivos y negativos\nc. Mostrar suma de pares\nd. Mayor de numeros impares\ne. Listar numeros ingresados\nf. Listar numero pares\ng. Listar las posiciones de los impares\nh. Salir\n Elija una opcion: ")
    match opcion:
        case "a":
            numeros = ingresar_numeros(5)
        case "b":
            if len(numeros) == 0:
                print("No se ha ingresado ningun dato.")
            else:
                cantidad_negativos_positivos = contar_positivos_negativos(numeros)
                print(f"La cantidad de positivos es {cantidad_negativos_positivos[0]} y la cantidad de negativos es {cantidad_negativos_positivos[1]}")
        case "c":
            if len(numeros) == 0:
                print("No se ha ingresado ningun dato")
            else:
                suma_pares = sumar_pares(numeros)
                print (f"La suma de los numeros pares es {suma_pares}")

        case "d":
            if len(numeros) == 0:
                print("No se ha ingresado ningun dato.")
            else:  
                mayor_impar = encontrar_mayor_impar(numeros)
                print(f"El mayor de los numeros impares es {mayor_impar}")

        case "e":
            if len(numeros) == 0:
                print("Usted no ha ingresado ningun dato.")
            else:
                for i in range(len(numeros)):
                    print(numeros[i])
        case "f":
            if len(numeros) == 0:
                print("No se ha ingresado ningun dato.")
            else:
                for i in range(len(numeros)):
                    if numeros[i] % 2 == 0:
                        print(numeros[i])
        case "g":
            if len(numeros) == 0:
                print("No se ha ingresado ningun dato.")
            else:
                posicion_impares = listar_posicion_impares(numeros)
                for i in range(len(posicion_impares)):
                    print(f"Hay un numero impar en la posicion: {posicion_impares[i]+1}")

        case "h":
            menu=False
        case _:
            print("Opcion no valida")
    system("pause")          
    system("cls")







