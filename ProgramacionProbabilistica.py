def calcular_probA(inicial):
    if inicial - 5000 < 0:
        return 0
    else:
        return 0.3 * (inicial - 5000) + 0.7 * (inicial + 5000)


def calcular_probB(inicial):
    return 0.9 * inicial + 0.1 * (inicial + 5000)


if __name__ == '__main__':
    pass
