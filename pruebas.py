# #### funciones
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

######### listas en python ejerccios
miLista=["maria","pepe","marta","antonio"]
print(miLista[3])
print(miLista[-2])
print(miLista[0:3])
print(miLista[1:])
miLista.insert(1,"adrian")
print(miLista)
print(miLista.index("adrian"))

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


# sacando la raiz cuadrada de un numero

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


# entramos en ciclo for


##########################################

# for i in ["primavera ", "otoño ", "invierno"]:
#     print(i)

# lo que se ouede hacer con el range
# for i in range(50, 111,1):
#     print("valor de la variable " + str(i))


# # verificar un correo electronico
# contador = 0

# correo = input("dijite su correo electronico : ")

# for i in correo:
#     if i == "@" or i == ".":
#         contador = contador+1

# if contador >= 2:
#     print("email es correcto")
# else:
#     print("el email es incorrecto")


# #utilizando la sinstruccione pass else y continue dentro de los bucles
# for i in "adrian":
#     if i == "r":
#         continue

#     print("imprimiendo la letra " + str(i))
##########

# # verificando numer de cel
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