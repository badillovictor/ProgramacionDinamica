def calcular_distancia(origen, destino, futuro):
    if grafo[destino][origen] != -1:
        return grafo[destino][origen] + futuro
    else:
        return 0


def obtener_destinos(origen):
    destinos = []
    for i in range(len(grafo[origen])):
        if not grafo[origen][i] == -1:
            destinos.append(i)
    return destinos


def obtener_origenes(destino):
    origenes = []
    for i in range(len(grafo)):
        if not grafo[i][destino] == -1:
            origenes.append(i)
    return origenes


def print_tabla(origenes, n, optimos):
    if not n == 0:
        encabezado = '\t'.join(['s{0}'.format(n),
                                '\t'.join([diccionario[i] for i in origenes]),
                                'f*(s{0})'.format(n)
                                # ,'x*({0})'.format(n),
                                ])
        print(encabezado)
        destinos = set()
        for e in origenes:
            destinos.update(obtener_destinos(e))
        soluciones = []
        nuevos_optimos = []
        for i in destinos:
            solucion = [diccionario[i]]
            for j in range(len(origenes)):
                solucion.append(str(calcular_distancia(i, origenes[j], int(optimos[j]))))
            solucion.append(str(max(solucion[1:])))
            nuevos_optimos.append(max(solucion[1:]))
            soluciones.append(solucion)
        for s in soluciones:
            print('\t'.join(s))
        print('\n')
        print_tabla(list(destinos), n - 1, nuevos_optimos)


grafo = [
    [-1, 130, 100, 80, 70, 50, 0, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, 20, 0, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, 45, 20, 0, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, 75, 45, 20, 0, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, 110, 75, 45, 20, 0, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, 150, 110, 75, 45, 20, 0, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 45],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 70],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 90],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 105],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 120],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
]

diccionario = {
    0: 'N',
    1: 'M',
    2: 'L',
    3: 'K',
    4: 'J',
    5: 'I',
    6: 'H',
    7: 'G',
    8: 'F',
    9: 'E',
    10: 'D',
    11: 'C',
    12: 'B',
    13: 'A',
}

if __name__ == '__main__':
    print_tabla([0], 3, [0])