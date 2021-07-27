
###### importando un modulo y mirando sus funcinalidades###############
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