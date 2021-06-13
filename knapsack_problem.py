def morral(tamano_morral, pesos, valores, n):

    if n == 0 or tamano_morral == 0:
        return 0

    if pesos[n - 1] > tamano_morral:
        return morral(tamano_morral, pesos, valores, n - 1)

    return max(valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1),
                morral(tamano_morral, pesos, valores, n - 1))


if __name__ == '__main__':
    valores = [60, 100, 120, 70, 400]
    pesos = [10, 20, 30, 40, 50]
    tamano_morral = int(input("Ingrese tamaño del morral: "))
    n = len(valores)

    resultado = morral(tamano_morral, pesos, valores, n)
    print("Tu mejor combinación de pesos y valores es", resultado)