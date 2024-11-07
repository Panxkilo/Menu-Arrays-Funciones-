
def encontrar_mayor_impar(lista:list)->list:
    maximo = lista[0]
    for i in range(len(lista)):
        if maximo < lista[i] and maximo % 2 != 0:
            maximo = lista[i]
    return maximo 

def listar_posicion_impares(lista:list)->list:
    posicion = -1
    lista_posiciones = []
    for i in range(len(lista)):
        posicion += 1
        if lista[i] % 2 != 0:
            lista_posiciones.append(posicion)
    return lista_posiciones








