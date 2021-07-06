def divisor(numero):
    divisor = []
    for i in range(1, numero + 1):
        if numero % i == 1:
            divisor.append(i)
    return divisor


def run():
    try:
        numero = int(input("dijite un numero: "))
        print(divisor(numero))
        print("termino el programa")
    except ValueError:
        print(" no se pueden letras solo numeros")


if __name__ == '__main__':
    run()
