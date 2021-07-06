#########trabajos de adrians tiven jimenez cardenas#####################


# # ################################################### metodos python #########################################################
# nombre = "aDrIaN"
# # pone los nombre minusculas
# nombre = nombre.lower()
# # pone los nombre en m mayuscula
# nombre = nombre.upper()
# # cuanta cuantas vese esta la "a" en adrian
# nombre.count("a")
# print(nombre)


# ################################## metodos en lista################################
# lista = [2, 7, 8, 14, 8]
# # cuenta cuantos caracteres tien mi lista en
# catidaenlalista = len(lista)
# # busca el elemento mas mas alto de la  lista de
# print(max(lista))
# # busca el numero mas pequeño de la  lista
# print(min(lista))
# ###############################ahñadir####################
# # agregar elementos a mi lista de
# lista.append("adrian")
# #agregando listas dentro de lista
# lista.append([12,23,"jimenez"])
# #agregando los numero del 1 al 9 en la lista y los pone de ultimos
# lista.extend(range(1,10))
# #me permite agregar varios objetos a la lista como tal no dentro de nada
# lista.extend([100,101,1002])
# #agrega un objeto en la pocicion que tu le des, y lo que quieres agregar
# lista.insert(1,100000)
# ################################eliminar####################
# #elimina el numero que le indiques
# lista.remove("adrian")
# # ordenas los datos  de la lista de
# ordenenlalista = lista.sort()
# # ver los elementos de la lista alreves
# alreverlista = lista.reverse()

# print(lista)


# ###################datos relevantes

# verifica cuantas veses cabe el 10 en 20
# prueba = 20//10
# print(prueba)


# ############################################################ funciones
# def mensaje():
#     print("hola mi nombre es adrian y estoy creando esta funcion")
#     print("tengo 18 años y estoy aprendiendo python")


# mensaje()

# ###funciones con parametros
# def suma(numero1, numero2):
#     print(numero1+numero2)


# suma(5, 5)

# suma(10, 10)

# suma(10, 20)

# ################################################################## listas en python ejerccios
# miLista = ["maria", "pepe", "marta", "antonio", ["adriann", 12,34]]
# #ingresando a un atupla dentro de otra tupla
# print(miLista[4][0])
# #imprimiendo el objeto marta de la lista
# print(miLista[3])
# #imprimiendo alrever la lita y imprimiendo antonio
# print(miLista[-2])
# #imprimiendo maria hasta el 3
# print(miLista[0:3])
# #imprimiendo de pepe hasta dond eacabe la lista
# print(miLista[1:])
# #cambiando un objeto por otro
# miLista.insert(1, "adrian")
# # te dice la  paccion de ese nombre
# print(miLista.index("adrian"))
# print(miLista)


# ################################################################## ejerccios de tupla
# tupla = ("juan", 13, 1, 1995)
# print(tupla[2])

# tupla = ("juan", 13, 1, 1995)
# # combertir tuplas en listas y viseversa con "tuple"
# milista = list(tupla)
# print(milista)
# # imprimiendo si ese nombre o varable esta en en la lista tupla
# print("juan" in milista)
# # contar cuantas veses hay un avariable en la listas o tuplas
# print(milista.count("juan"))
# # contar cuantos caracteres tien en este caso mi listas
# print(len(milista))

############################################################# ejerccios de diccionario
midiccionario = {"alemania": "berlin", "francia": "paris", 23: "jordan",
                 "reino unido": "londres", "esapña": "madrid"}
print(midiccionario["irlanda"])
# agregando mas paise y su capital
midiccionario["colombia"] = "barranquillla"
print(midiccionario)
# cambiandole la capital a colombia
midiccionario["colombia"] = "bogota"
print(midiccionario)
# eliminando elemto ,reino unido y su capital
del midiccionario["reino unido"]
print(midiccionario)
middicionario = {23: "jordan", "nombre": "michael", "adrian": "stiven",
                 "brayan": "andres", "anillos": {"temporadas": [1991, 1992, 1993, 1994, 1995, 1996]}}
# ingresar a 1993 jajja imbentado por mi
print(middicionario["anillos"]["temporadas"][2])
# imprimir todas las llaver del diccionario
print(middicionario.keys())
# imprimir los valores de las llaves
print(middicionario.values())
print(len(middicionario))


# ########################################################condicionales
# notas=int(input("dijite su nota: "))

# def evaluacion(notas):
#     valoracion="aprobado"
#     if notas < 5:
#         valoracion="no,aprobado"
#     return valoracion

# print(evaluacion(notas))

# #######utilizando in para ver que si crelegida esta en careras
# careras = ["ingeniero", "programador", "docente","tutor"]
# print("escoga la  carrera que desee: ingeniro, programdor, docente, tutor ")
# crelegida=input("dijite su carrera escogida: ")
# # poniendo lo escriba  en minuscula, tambien esta upper()
# crelegida=crelegida.lower()
# if crelegida in careras:
#     print("la carrera elegida es " + crelegida)
# else:
#     print("eligio una carrera que no esta en la listas")

# trabajo del instructor oscar ####################################333
# ######################taller des profesor oscar 1:
# nombre = input("dijite su  nombre: ")
# mensualidad = int(input("dijite su  mensualidad: "))
# edad = int(input("dijite su  edad: "))
# sexo = input("dijite su sexo M o F: ")
# sexo = sexo.upper()

# if sexo == "M" and mensualidad < 1200000:
#     print("usted " + nombre + " se encuentra en la categoria #a ")

# elif sexo == "F" and mensualidad > 4000000:
#     print("usted "+ nombre + " se encuentra en la categoria #b")

# elif sexo == "F" and edad > 20 or edad < 30 and mensualidad > 1200000 or mensualidad < 4000000:
#     print("usted "+ nombre + " se encuentra en la categoria #c")


# #################ejercico numero 2
# ingresos = int(input("por favor dijite su ingresos: "))
# estado_civil = input("dijite S si esta soltero o C si esta casado: ")
# estado_civil = estado_civil.upper()
# tiene_hijos = input("dijite si tien hijos escreiba SI o NO: ")
# tiene_hijos = tiene_hijos.upper()


# print(estado_civil)
# if ingresos > 20000000:
#     print("el credito se cosede")
# elif ingresos < 20000000 or ingresos > 12000000 and estado_civil == "S":
#     print("se consede el prestamo")
# if ingresos > 15000000 or ingresos < 20000000 and estado_civil == "s" and tiene_hijos == "SI":
#     print("se le consede el prestamo")
# else:
#     print("lo siento el prestamo no se le cosede")


# # ####################ejercicio numero 5

# horas_trabajadas = int(input("digite la cantidad de horas que trabaja: "))
# pago_hora = float(input("digite el pago por cada hora: "))

# if horas_trabajadas > 48:
#     triple = horas_trabajadas-48
#     sueldo = 40*pago_hora+(8*pago_hora*2)+(triple*pago_hora*3)
# elif horas_trabajadas > 10:
#     doble = horas_trabajadas-40
#     sueldo = 40*pago_hora+(doble*pago_hora*2)
# else:
#     sueldo = horas_trabajadas*pago_hora
# print("el sueldo total por las", horas_trabajadas,
#       "horas trabajadas es: $", sueldo)


######################ejercico de ciclos con el instructo oscar vanegas#####################
# 2. Realiza el código correspondiente al siguiente ejemplo de ejecución de un programa en Python, a
# través de la estructura while y condicional elif.

# pregunta = "si"
# while pregunta == "si":
#     print("Que quieres hacer hoy? Escribe una opción: ")
#     print(" 1 para Saludar")
#     print(" 2 para Sumar dos numeros")
#     print(" 3 para Salir")
#     respuesta = int(input("ingrese su respuesta su  respuesta: "))
#     if respuesta == 2:
#         numero_1 = int(input("ingresa un numero: "))
#         numero_2 = int(input("ingresa otro numero para sumar: "))
#         print(f"este es el resultado de la suma es {numero_1+numero_2}")
#     elif respuesta == 1:
#         print("hola como estas?, espero que estes bien: ")
#     elif respuesta == 3:
#         print("gracias por poner aprueba mi codigo")
#         break
#     else:
#         print("lo sinto dijite un numero que este en el los que se piden")

# ######### ejercio 3 del profesor oscar mauricio
# contraseña = input("por favor dijite su contraseña: ")
# contraseña2 = input("por favor dijite su contraseña para comprobarla: ")
# intentos = 1
# while contraseña2 != contraseña:
#     print("lo siento su contraseña no coinside dijitela de nuevo")
#     contraseña2 = input("por favor dijite su contraseña para comprobarla: ")
#     intentos += 1
#     if intentos == 3:
#         print("lo siento an consumido muchos intentos")
#         break
# else:
#     print("gracias po ringresar su contraseña")


#################################################################trabajo del instructor oscar /####################################

# ################################################### ciclo while
# i=1
# while i<=12:
#     print("ejecusion de ", str(i))
#     i=i+1


# primeras pruebas de ciclo while
# edad = int(input("dijite su edad :"))

# while edad<5 or edad>12:
#         print("has introducido una edad negativa escriba por favor un logica positiva")
#         edad = int(input("dijite su edad"))
# print("gracias por colavorar")
# print("su edad es "+ str(edad))


# ###########ejrciio 4 del instructor oscar mauricio
# numeropares= int(input("dijite un nuemero par: "))

# while numeropares % 2 != 0:
#     print(" lo sinto tu numero no es par dijitelo nuevamente")
#     numeropares= int(input("dijite un nuemero par: "))


# ####################sacando la raiz cuadrada de un numero

# import math

# def mensaje():
#     print("hola como estas dijite su numero que desea sacare la raiz cauadrada")

# mensaje()

# numero = int(input("dijite un numero :"))

# intentos=0

# while numero<0:
#     print("no se puede allar la raiz de este numero ")

#     numero = int(input("dijite un numero :"))
#     if numero<0:
#         intentos=intentos+1

#     if intentos == 5:
#         print("a sconsumidos muchos intentos")
#         break;

# if intentos<2:
#     solucion=math.sqrt(numero)
#     print("la raiz cuadrada de " + str(numero) + " es " + str(round(solucion,2)))


# preguntado al usuarios su edad ,tiene 3 intentos para ponerl acorrecta
# edad = int(input("dijite su edad : "))

# intentos = 1

# while edad < 10 or edad > 111:
#     print("es imposible tener esa edad dijite la eda de nuevo")
#     edad = int(input("dijite su edad : "))

#     intentos = intentos+1
#     if intentos == 3:
#         print("lo sinto a consumido muchos intentos intente en otro momento")
#         break;


# if intentos<3:
#     print("gracias por introducir su edad, su edad es " + str(edad))


# #ejercios echo por el instructor
# sumaedades = 0
# personas = 0

# while personas<4:
#     notas=int(input(" por favor dijte sus notas "))
#     sumaedades = sumaedades + notas
#     personas=personas+1

# promedio = sumaedades/4
# print("su promedio es " + str(promedio))


##########################################


# ###############################################################3 entramos en ciclo for


##########################################

# for i in ["primavera ", "otoño ", "invierno"]:
#     print(i)

# lo que se ouede hacer con el range
# for i in range(50, 111,1):
#     print("valor de la variable " + str(i))


# ######### verificar un correo electronico
# contador = 0

# correo = input("dijite su correo electronico : ")

# for i in correo:
#     if i == "@" or i == ".":
#         contador = contador+1

# if contador >= 2:
#     print("email es correcto")
# else:
#     print("el email es incorrecto")


# ######utilizando la sinstruccione pass else y continue dentro de los bucles
# for i in "adrian":
#     if i == "r":
#         continue

#     print("imprimiendo la letra " + str(i))
##########

# ######### verificando numer de cel
# cel = (input("dijite su numero celular: "))
# for i in cel:
#     if i != 10:
#         print("lo siento su numer no puede contener mas de 10")
#         cel = int(input("dijite su numero celular: "))

# if i==10:
#     print(" su numero es " + str(cel))

# def mensaje():
#     print("""   por favor dijite su contraseña no tiene que tener numeros, y recuerde que nada mas tiene 3 intentos""")

# mensaje()
# contraseña = input("dijite su contraseña ")


# ########pidiendo numro a usuario
# cel = (input("dijite su numero celular: "))

# valueLength = len(cel)

# if valueLength != 10:
#     print("te falto o te psaste de numeros")
# else:
#     print("bacano")


# #####imprimiedo las edades cumplias
# edad = int(input("¿Cuántos años tienes? "))
# for i in range(edad):
#     print("Has cumplido " + str(i+1) + " años")


# ###### intenta averiguar qu esta haciedp
# numero = int(input("Introduce un número entero positivo: "))
# for i in range(1, numero+1, 2):
#     print(i, end=", ")

# edad=input("dijite su edad: ")
# while edad<10 or edad>100:
#     print("por favor dijite una edad adecuada")

# pidiendo numro a usuario

# ########jercicio echo po mi
# print("buenos dias como esta espero que bien que quieres hacer el dia de hoy ")
# print("estas son las opcione que tenemos 1 para registrarse")
# opcione = int(input("dijite su opcion "))

# intentos = 1
# while opcione != 1:
#     print("lo sinto dijite el numero correcto")
#     intentos += 1
#     opcione = int(input("dijite su opcion "))
#     if intentos > 3:
#         print("lo siento a consumido mucho intentos")
#         break

# if opcione == 1:
#     print("gracias por entrar en la secion de  registro")
#     #dijitando nombre
#     nombre = input("dijite su nombre: ")
#     #dijitando edad
#     edad = int(input("dijite su edad: "))
#     while edad < 4 or edad > 100:
#         print("su edad no puede ser " + str(edad) + " dijitela de nuevo ")
#         edad = int(input("dijite su edad: "))
#     #dijitando correo
#     contador = 0
#     correo = input("dijite su correo electronico : ")
#     for i in correo:
#         if i == "@" or i == ".":
#             contador = contador+1
#     if contador >= 2:
#         print("email es correcto")
#     else:
#         print("el email es incorrecto")
#         print("su nombre es :" + nombre + " y su edad es :" + str(edad) +
#           " gracias ya tenemos todos su registros que necesitamos ")

# ###########################################################ejerccios de generadores ojo
# def generapares(limite):
#     numero1 = 1
#     milista = []
#     while numero1 < limite:
#         milista.append(numero1*2)
#         numero1 += 1
#     return milista

# print(generapares(10))

# ########
# def generapares(limite):
#     numero1 = 1
#     while numero1 < limite:
# # yield contien los numeros
#         yield numero1*2
#         numero1 += 1
# contenedordefuncion=generapares(10)
# print(next(contenedordefuncion))
# print("aqui podria ir mas codigo....")
# print(next(contenedordefuncion))

# ###practica generadores ll
# #el * es para poder insertar los parametros que desees
# def devuelve_valores(*ciudades):
#     for palabras in ciudades:
#         #for letra in palabras:
#             yield from palabras

# contendo_ciudadaes=devuelve_valores("madrid", "barcelona","bilbao","valencia")

# print(next(contendo_ciudadaes))
# print(next(contendo_ciudadaes))
# print(next(contendo_ciudadaes))
# print(next(contendo_ciudadaes))

# ###### ejerccios de excepciones
# numero1= int(input("dijite un numero 1: "))
# numero2= int(input("dijite un numero 2: "))
# def divide(numero1, numero2):
#     #sirve por si ahy un error, siga corriendo el codigo normal
#     try:
#         return numero1 / numero2
#     except  ZeroDivisionError:
#         print("lo sinto no se puede dividir por cero")
# print(divide(numero1, numero2))
# print("gracias por insertar los numeros")

# # ######
# def divide():
#     try:
#         op1=float(input("introduce el primer numero: "))
#         op2=float(input("introduce el segundo numero: "))
#         print("la divison es " + str(op1/op2))
#     except ValueError:
#         print("el valor introducido es erroneo")
#         #pone esto mas el nombre del ERROR que te da en la consola
#     except ZeroDivisionError:
#         print("no se puede dividir por cero")
#         #hacer qu esta linea se ejecute siempre con finally
#     finally:
#         print("calculo finalizado")

# divide()


# # programacion orientada a objetos POO
# # calses
# class Coche():
#     # propiedades de la clase
#     largoChasis = 250
#     anchoChasis = 120
#     rueda = 4
#     enMarcha = False

#     # metodo o comportamiento, de la clase
#     def arrancar(self):
#         # argumento o paramtro self
#         self.enMarcha = True

#     def estado(self):
#         if self.enMarcha:
#             return "el coche esta en marcah"
#         else:
#             return "el coche esta paraddo"


# # crear objeto o instancia, binculado a la  clase
# miCoche = Coche()
# # mostrar desde el objet  lo que tiene la clase por dentro
# print("el largo del coche es: " + str(miCoche.largoChasis))
# print("mi coche tien " + str(miCoche.rueda))
# # llamando el metodo arrancar
# miCoche.arrancar()
# # imprimiendo el metodo de stado
# print(miCoche.estado())


# # #####
# # clase
# class Coche():
#     # funcion de tipo constructor, es el estado inicial de las propiedades
#     def __init__(self):

#         # propiedades de la clase
#         self.largoChasis = 250
#         self.anchoChasis = 120
#         # encapsulando propiedades para que no se puedan modifcar desde afuera de la clase
#         self.__rueda = 4
#         self.__enMarcha = False

#     # metodo o comportamiento, de la clase
#     def arrancar(self, arrancamos):
#         self.__enMarcha = arrancamos

#         if self.__enMarcha == True:
#             chequeo = self.__chequeo_interno()

#         if self.__enMarcha == True and chequeo == True:
#             return "el coche esta en marcah"

#         elif self.__enMarcha == True and chequeo == False:
#             return "algo a ido mal en el chequeo , no podemos arrancar"

#         else:
#             return "el coche esta paraddo"

#     def estado(self):
#         print("mi coche tiene" + str(self.__rueda) + "ruedas. un ancho de " +
#               str(self.anchoChasis) + "y un largo de" + str(self.largoChasis))

#     # encapsulando el metodo com __ y al llamarlo tambien tenemos que colocarles esa rallita
#     def __chequeo_interno(self):
#         print("realizando chequeo interno")

#         self.gasolina = "ok"
#         self.aceite = "ok"
#         self.puertas = "cerradas"

#         if self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas":
#             return True
#         else:
#             return False


# # crear objeto o instancia, binculado a la  clase
# miCoche = Coche()
# # mostrar desde el objet  lo que tiene la clase por dentro
# print("el largo del coche es: " + str(miCoche.largoChasis))
# # llamando el metodo arrancar
# print(miCoche.arrancar(True))
# # llamando el metodo de stado-
# miCoche.estado()

# print("------------------A continuacion crearemos el segundo objeto--------------------")

# miCoche2 = Coche()
# print(miCoche2.arrancar(False))
# miCoche2.estado()


# ####################super clase, herecias.#############
# class vehiculos():

#     def __init__(self, marca, modelo):

#         self.marca = marca
#         self.modelo = modelo
#         self.enmarcha = False
#         self.acelera = False
#         self.frena = False

#     def arrancar(self):
#         self.enmarcha = True

#     def acelerar(self):
#         self.acelera = True

#     def frenar(self):
#         self.frena = True

#     def estado(self):
#         print(f"marca: {self.marca} \n modelo: {self.modelo} \n en marcah: {self.enmarcha} \n acelera: {self.acelera} \n frena: {self.frena}")


# class furgoneta(vehiculos):

#     def carga(self, cagar):
#         self.cargado = cagar
#         if self.cargado == True:
#             return"la furgoneta esta cargada"
#         else:
#             return"la furgoneta no esta cargada"

# # para eredar tienes que psarle por parametro el nombre de la calse que quieres heredar


# class moto(vehiculos):

#     hcaballito = ""

#     def caballito(self):
#         self.hcaballito = "voy haciendo el caballito"

#     def estado(self):
#         print(f"marca: {self.marca} \n modelo: {self.modelo} \n en marcah: {self.enmarcha} \n acelera: {self.acelera} \n frena: {self.frena} \n {self.hcaballito}")


# class Velectricos(vehiculos):
#     # teenemos que pasarle los parametros de clase vehiculos
#     def __init__(self, marca, modelo):
#         # trae los parametros de la clase paadre en este caso vehiculos
#         super().__init__(marca, modelo)
#         self.autonomia = 100

#     def cargarEnergiar(self):
#         self.cargando = True


# miMoto = moto("honda", "CBR")

# miMoto.caballito()

# miMoto.estado()


# mifurganeta = furgoneta("reanul", "kangoo")

# mifurganeta.arrancar()

# mifurganeta.estado()

# print(mifurganeta.carga(True))


# class bicicletaElectrica(Velectricos, vehiculos):
#     pass


# mibici = bicicletaElectrica("honda", "hj")
# verificando si uns instacia pertenece a un clase
# print(isinstance(miMoto, vehiculos))


# #########polimorfismo en pogramacion orientada a objetos##############

# class coche():

#     def desplazamiento(self):
#         print("me despalzo utilizando 4 ruedas")


# micoche = coche()


# class moto():

#     def desplazamiento(self):
#         print("me desplazo utilizando 2 ruedas")


# mimoto = moto()


# class camion():

#     def desplazamiento(self):
#         print("me desplazo utilizando 6 ruedas")


# micamion = camion()
# # polimorfismo


# def desplazamientodevehiculos(vehiculo):
#     vehiculo.desplazamiento()


# desplazamientodevehiculos(micamion)


# ##################### funcio lambda ###################
# ##########3######funcion,parametroslos 2 puntos son para retornar base*altura
# area_triengulo = lambda base, altura:(base*altura)/2

# print(area_triengulo(2, 7))

# print(area_triengulo(30,12))

# ##elevar al cubo###########

# al_cubo = lambda numero:(numero**3)
# print(f"este es la el resutado  {al_cubo(3)}")

# #####################funcion filter ###############

# #filtrando solo numeros pares
# numeros = [17, 24, 7, 39, 8, 51, 92]

# print(list(filter(lambda numero_par: numero_par % 2 == 0, numeros)))

##################funcion map ####################


import math

numero = int(input("dijite un numero: "))

#modulo
if math.fmod(numero,2) == 0:
    print(f"su numero es par {math.fmod(numero,2)}")
else:
    print("su numero no es par")

#elevado al cuadradado
if math.exp(numero):
    print(f"su numero es par {math.exp(numero)}")
else:
    print("su numero no es par")

# la potencia de un numer elevado a otro numero potencia
if math.pow(numero,2):
    print(f"su numero es par {math.pow(numero,2)}")
else:
    print("su numero no es par")

#sacando la raix cuadrada de un numero
if math.sqrt(numero):
    print(f"su numero es par {math.sqrt(numero)}")
else:
    print("su numero no es par")