def divisor(numero):
    divisor = []
    for i in range(1, numero + 1):
        if numero % i == 1:
            divisor.append(i)
    return divisor


def run():
    numero = (input("dijite un numero: "))
    ####si numero es numero, y si no ,,, solo se puede ingresar numeros##########
    assert numero.isnumeric(),"solo se puede ingresar numeros"
    print(divisor(int(numero)))
    print("termino el programa")


if __name__ == '__main__':
    run()
