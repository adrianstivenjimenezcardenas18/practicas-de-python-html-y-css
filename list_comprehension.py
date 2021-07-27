def run():
    lista = []
    for i in range(1, 101):
        if i % 2 == 0:
            lista.append(i**2)
    print(lista)

    # con lis comprenhension

    listas = [i**2 for i in range(1, 10) if i % 2 == 0]

    print(listas)

    muliplos_4 = [i for i in range(1, 10) if i > 5]
    print(muliplos_4)

    ####################30
    numero_impares = [i for i in range(100) if i % 2 == 0]
    print(numero_impares)

# esta es la rama de adrian
if __name__ == '__main__':
    run()
