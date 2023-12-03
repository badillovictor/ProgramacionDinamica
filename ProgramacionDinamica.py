def calcular_distancia(origen, destino, futuro = 0):
    return grafo[destino][origen] + futuro


def obtener_destinos(origen):
    destinos = []
    for i in range(len(grafo[origen])):
        if not grafo[origen][i] == 100:
            destinos.append(i)
    return destinos


def obtener_origenes(destino):
    origenes = []
    for i in range(len(grafo)):
        if not grafo[i][destino] == 100:
            origenes.append(i)
    return origenes


def print_tabla(origenes, n):
    if not n == 0:
        encabezado = '\t'.join(['s{0}'.format(n),
                              '\t'.join([diccionario[i] for i in origenes]),
                              'f*(s{0})'.format(n)
                              #,'x*({0})'.format(n),
                              ])
        print(encabezado)
        destinos = set()
        for e in origenes:
            destinos.update(obtener_destinos(e))
        soluciones = []
        for i in destinos:
            solucion = []
            solucion.append(diccionario[i])
            for j in origenes:
                solucion.append(str(calcular_distancia(i, j)))
            solucion.append(str(min(solucion[1:])))
            soluciones.append(solucion)
        for s in soluciones:
            print('\t'.join(s))
        print('\n')
        print_tabla(destinos, n-1)



grafo = [
    [100, 4, 3, 100, 100, 100, 100, 100, 100, 100],
    [100, 100, 100, 3, 3, 4, 100, 100, 100, 100],
    [100, 100, 100, 3, 6, 1, 100, 100, 100, 100],
    [100, 100, 100, 100, 100, 100, 5, 4, 6, 100],
    [100, 100, 100, 100, 100, 100, 1, 2, 4, 100],
    [100, 100, 100, 100, 100, 100, 4, 3, 7, 100],
    [100, 100, 100, 100, 100, 100, 100, 100, 100, 3],
    [100, 100, 100, 100, 100, 100, 100, 100, 100, 4],
    [100, 100, 100, 100, 100, 100, 100, 100, 100, 2],
    [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
]

diccionario = {
    0: 'J',
    1: 'I',
    2: 'H',
    3: 'G',
    4: 'F',
    5: 'E',
    6: 'D',
    7: 'C',
    8: 'B',
    9: 'A',
}

if __name__ == '__main__':
    print_tabla([0], 4)
