#r es para leer el archivos
#w es para sobreescribir en el archivos
# a para adicionar al archivo


def read():
    numeros = []
    #leyendo los numero que se encuantran dentro de ese archiv
    with open("./archivos/numeros.txt", "r", encoding="utf-8") as f:
        for linea in f:
            numeros.append(int(linea))
    print(numeros)


def write():
    names = ["facundo","miguel", "cristian","rocío","adrian"]
    #anadiendo names.txt a archivos y añadiendo datos
    with open("./archivos/names.txt", "a", encoding="utf-8") as n:
        for name in names:
            n.write(name)
            n.write("\n")


def run():
    write()


if __name__ == '__main__':
    run()
