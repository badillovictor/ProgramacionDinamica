def calcular_probA_inicial(actual):
    if actual == 0:
        return 0
    else:
        return int(0.3 * (actual - 5000) + 0.7 * (actual + 5000))


def calcular_probB_inicial(actual):
    if actual == 0:
        return 0
    else:
        return int(0.9 * actual + 0.1 * (actual + 5000))


def calcular_probA(actual, x, y):
    if actual == 0:
        return 0
    else:
        return int(0.3 * x + 0.7 * y)


def calcular_probB(actual, x, y):
    if actual == 0:
        return 0
    else:
        return int(0.9 * x + 0.1 * y)


def print_tabla_inicial(n, diccionario):
    encabezado = ('\t'*2).join(['s{0}'.format(n),
                            ('\t'*2).join(['A', 'B']),
                            'f*(s{0})'.format(n)
                            # ,'x*({0})'.format(n),
                            ])
    print(encabezado)
    nuevodict = {}
    for e in diccionario:
        solucion = [str(diccionario[e])]
        solucion.append(str(calcular_probA_inicial(diccionario[e])))
        solucion.append(str(calcular_probB_inicial(diccionario[e])))
        solucion.append(str(max(solucion[1:])))
        nuevodict[diccionario[e]] = int(float(max(solucion[1:])))
        print('\t'.join(solucion))
    print('\n')
    print_tabla_posterior(n-1, nuevodict)


def print_tabla_posterior(n, diccionario):
    if not n == 0:
        encabezado = ('\t'*2).join(['s{0}'.format(n),
                                ('\t'*2).join(['A', 'B']),
                                'f*(s{0})'.format(n)
                                # ,'x*({0})'.format(n),
                                ])
        print(encabezado)
        nuevodict = {}
        keys = list(diccionario.keys())
        for e in diccionario.keys():
            solucion = [str(e)]
            if e == 0:
                solucion.append('0')
                solucion.append('0')
            else:
                solucion.append(str(calcular_probA(e, diccionario[e - 5000], diccionario[e + 5000])))
                solucion.append(str(calcular_probB(e, diccionario[e], diccionario[e + 5000])))
            solucion.append(str(max(solucion[1:])))
            nuevodict[e] = int(max(solucion[1:]))
            print('\t'.join(solucion))
        print('\n')
    print_tabla_posterior(n - 1, nuevodict)


if __name__ == '__main__':
    print_tabla_inicial(3, {
        0: 0,
        5000: 5000,
        10000: 10000,
        15000: 15000,
    })
