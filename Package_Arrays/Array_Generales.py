from Package_Input.Funciones_Input import *
def ingresar_numeros(cantidad:int):
    numeros = []
    for i in range(cantidad):
         numero = get_int("Ingrese 10 numeros del -1000 al 1000: ",-1000,1000,"Reingrese el numero: ")
         numeros.append(numero)
    return numeros
def contar_positivos_negativos(lista:list)->list:
    contador_positivos = 0
    contador_negativos = 0
    for i in range(len(lista)):
        if lista[i] > 0:
            contador_positivos += 1
        elif lista[i] < 0:
            contador_negativos += 1
    lista_contadores = [contador_positivos,contador_negativos]
    return lista_contadores 
def sumar_pares(lista:list)->int:
    acumulador=0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            acumulador = acumulador + lista[i]
    return acumulador