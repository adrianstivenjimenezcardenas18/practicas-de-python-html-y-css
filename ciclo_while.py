################################################### ciclo while
i=1
while i<=12:
    print("ejecusion de ", str(i))
    i=i+1


###primeras pruebas de ciclo while
edad = int(input("dijite su edad :"))

while edad<5 or edad>12:
        print("has introducido una edad negativa escriba por favor un logica positiva")
        edad = int(input("dijite su edad"))
print("gracias por colavorar")
print("su edad es "+ str(edad))


###########ejrciio 4 del instructor oscar mauricio
numeropares= int(input("dijite un nuemero par: "))

while numeropares % 2 != 0:
    print(" lo sinto tu numero no es par dijitelo nuevamente")
    numeropares= int(input("dijite un nuemero par: "))


####################sacando la raiz cuadrada de un numero

import math

def mensaje():
    print("hola como estas dijite su numero que desea sacare la raiz cauadrada")

mensaje()

numero = int(input("dijite un numero :"))

intentos=0

while numero<0:
    print("no se puede allar la raiz de este numero ")

    numero = int(input("dijite un numero :"))
    if numero<0:
        intentos=intentos+1

    if intentos == 5:
        print("a sconsumidos muchos intentos")
        break;

if intentos<2:
    solucion=math.sqrt(numero)
    print("la raiz cuadrada de " + str(numero) + " es " + str(round(solucion,2)))


####preguntado al usuarios su edad ,tiene 3 intentos para ponerl acorrecta
edad = int(input("dijite su edad : "))

intentos = 1

while edad < 10 or edad > 111:
    print("es imposible tener esa edad dijite la eda de nuevo")
    edad = int(input("dijite su edad : "))

    intentos = intentos+1
    if intentos == 3:
        print("lo sinto a consumido muchos intentos intente en otro momento")
        break;


if intentos<3:
    print("gracias por introducir su edad, su edad es " + str(edad))


#ejercios echo por el instructor
sumaedades = 0
personas = 0

while personas<4:
    notas=int(input(" por favor dijte sus notas "))
    sumaedades = sumaedades + notas
    personas=personas+1

promedio = sumaedades/4
print("su promedio es " + str(promedio))