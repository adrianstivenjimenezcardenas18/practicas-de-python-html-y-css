# programacion orientada a objetos POO
# calses
class Coche():
    # propiedades de la clase
    largoChasis = 250
    anchoChasis = 120
    rueda = 4
    enMarcha = False

    # metodo o comportamiento, de la clase
    def arrancar(self):
        # argumento o paramtro self
        self.enMarcha = True

    def estado(self):
        if self.enMarcha:
            return "el coche esta en marcah"
        else:
            return "el coche esta paraddo"


# crear objeto o instancia, binculado a la  clase
miCoche = Coche()
# mostrar desde el objet  lo que tiene la clase por dentro
print("el largo del coche es: " + str(miCoche.largoChasis))
print("mi coche tien " + str(miCoche.rueda))
# llamando el metodo arrancar
miCoche.arrancar()
# imprimiendo el metodo de stado
print(miCoche.estado())


# #####
# clase
class Coche():
    # funcion de tipo constructor, es el estado inicial de las propiedades
    def __init__(self):

        # propiedades de la clase
        self.largoChasis = 250
        self.anchoChasis = 120
        # encapsulando propiedades para que no se puedan modifcar desde afuera de la clase
        self.__rueda = 4
        self.__enMarcha = False

    # metodo o comportamiento, de la clase
    def arrancar(self, arrancamos):
        self.__enMarcha = arrancamos

        if self.__enMarcha == True:
            chequeo = self.__chequeo_interno()

        if self.__enMarcha == True and chequeo == True:
            return "el coche esta en marcah"

        elif self.__enMarcha == True and chequeo == False:
            return "algo a ido mal en el chequeo , no podemos arrancar"

        else:
            return "el coche esta paraddo"

    def estado(self):
        print("mi coche tiene" + str(self.__rueda) + "ruedas. un ancho de " +
              str(self.anchoChasis) + "y un largo de" + str(self.largoChasis))

    # encapsulando el metodo com __ y al llamarlo tambien tenemos que colocarles esa rallita
    def __chequeo_interno(self):
        print("realizando chequeo interno")

        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas":
            return True
        else:
            return False


# crear objeto o instancia, binculado a la  clase
miCoche = Coche()
# mostrar desde el objet  lo que tiene la clase por dentro
print("el largo del coche es: " + str(miCoche.largoChasis))
# llamando el metodo arrancar
print(miCoche.arrancar(True))
# llamando el metodo de stado-
miCoche.estado()

print("------------------A continuacion crearemos el segundo objeto--------------------")

miCoche2 = Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()


####################super clase, herecias.#############
class vehiculos():

    def __init__(self, marca, modelo):

        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print(f"marca: {self.marca} \n modelo: {self.modelo} \n en marcah: {self.enmarcha} \n acelera: {self.acelera} \n frena: {self.frena}")


class furgoneta(vehiculos):

    def carga(self, cagar):
        self.cargado = cagar
        if self.cargado == True:
            return"la furgoneta esta cargada"
        else:
            return"la furgoneta no esta cargada"

# para eredar tienes que psarle por parametro el nombre de la calse que quieres heredar


class moto(vehiculos):

    hcaballito = ""

    def caballito(self):
        self.hcaballito = "voy haciendo el caballito"

    def estado(self):
        print(f"marca: {self.marca} \n modelo: {self.modelo} \n en marcah: {self.enmarcha} \n acelera: {self.acelera} \n frena: {self.frena} \n {self.hcaballito}")


class Velectricos(vehiculos):
    # teenemos que pasarle los parametros de clase vehiculos
    def __init__(self, marca, modelo):
        # trae los parametros de la clase paadre en este caso vehiculos
        super().__init__(marca, modelo)
        self.autonomia = 100

    def cargarEnergiar(self):
        self.cargando = True


miMoto = moto("honda", "CBR")

miMoto.caballito()

miMoto.estado()


mifurganeta = furgoneta("reanul", "kangoo")

mifurganeta.arrancar()

mifurganeta.estado()

print(mifurganeta.carga(True))


class bicicletaElectrica(Velectricos, vehiculos):
    pass


mibici = bicicletaElectrica("honda", "hj")
##verificando si uns instacia pertenece a un clase
print(isinstance(miMoto, vehiculos))


#########polimorfismo en pogramacion orientada a objetos##############

class coche():

    def desplazamiento(self):
        print("me despalzo utilizando 4 ruedas")


micoche = coche()


class moto():

    def desplazamiento(self):
        print("me desplazo utilizando 2 ruedas")


mimoto = moto()


class camion():

    def desplazamiento(self):
        print("me desplazo utilizando 6 ruedas")


micamion = camion()
# polimorfismo


def desplazamientodevehiculos(vehiculo):
    vehiculo.desplazamiento()


desplazamientodevehiculos(micamion)