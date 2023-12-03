def calcular_probA(inicial):
    if inicial - 5000 < 0:
        return 0
    else:
        return 0.3 * (inicial - 5000) + 0.7 * (inicial + 5000)


def calcular_probB(inicial):
    return 0.9 * inicial + 0.1 * (inicial + 5000)


def creacion_grafo(grafo: set, limite: int):
    if limite != 0:
        for e in grafo:
            if e != 0:
                grafo.update([e-5000, e, ])


if __name__ == '__main__':
    pass
