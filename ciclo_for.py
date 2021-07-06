###############################################################3 entramos en ciclo for


#########################################

for i in ["primavera ", "otoño ", "invierno"]:
    print(i)

####lo que se pouede hacer con el range######
for i in range(50, 111,1):
    print("valor de la variable " + str(i))


######### verificar un correo electronico
contador = 0

correo = input("dijite su correo electronico : ")

for i in correo:
    if i == "@" or i == ".":
        contador = contador+1

if contador >= 2:
    print("email es correcto")
else:
    print("el email es incorrecto")


######utilizando la sinstruccione pass else y continue dentro de los bucles
for i in "adrian":
    if i == "r":
        continue

    print("imprimiendo la letra " + str(i))
#########

######### verificando numer de cel
cel = (input("dijite su numero celular: "))
for i in cel:
    if i != 10:
        print("lo siento su numer no puede contener mas de 10")
        cel = int(input("dijite su numero celular: "))

if i==10:
    print(" su numero es " + str(cel))

def mensaje():
    print("""   por favor dijite su contraseña no tiene que tener numeros, y recuerde que nada mas tiene 3 intentos""")

mensaje()
contraseña = input("dijite su contraseña ")


########pidiendo numro a usuario
cel = (input("dijite su numero celular: "))

valueLength = len(cel)

if valueLength != 10:
    print("te falto o te psaste de numeros")
else:
    print("bacano")


#####imprimiedo las edades cumplias
edad = int(input("¿Cuántos años tienes? "))
for i in range(edad):
    print("Has cumplido " + str(i+1) + " años")


###### intenta averiguar qu esta haciedp
numero = int(input("Introduce un número entero positivo: "))
for i in range(1, numero+1, 2):
    print(i, end=", ")

edad=input("dijite su edad: ")
while edad<10 or edad>100:
    print("por favor dijite una edad adecuada")

######pidiendo numro a usuario

########jercicio echo po mi
print("buenos dias como esta espero que bien que quieres hacer el dia de hoy ")
print("estas son las opcione que tenemos 1 para registrarse")
opcione = int(input("dijite su opcion "))

intentos = 1
while opcione != 1:
    print("lo sinto dijite el numero correcto")
    intentos += 1
    opcione = int(input("dijite su opcion "))
    if intentos > 3:
        print("lo siento a consumido mucho intentos")
        break

if opcione == 1:
    print("gracias por entrar en la secion de  registro")
    #dijitando nombre
    nombre = input("dijite su nombre: ")
    #dijitando edad
    edad = int(input("dijite su edad: "))
    while edad < 4 or edad > 100:
        print("su edad no puede ser " + str(edad) + " dijitela de nuevo ")
        edad = int(input("dijite su edad: "))
    #dijitando correo
    contador = 0
    correo = input("dijite su correo electronico : ")
    for i in correo:
        if i == "@" or i == ".":
            contador = contador+1
    if contador >= 2:
        print("email es correcto")
    else:
        print("el email es incorrecto")
        print("su nombre es :" + nombre + " y su edad es :" + str(edad) +
          " gracias ya tenemos todos su registros que necesitamos ")