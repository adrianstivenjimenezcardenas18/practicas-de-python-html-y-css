########################################################condicionales
notas=int(input("dijite su nota: "))

def evaluacion(notas):
    valoracion="aprobado"
    if notas < 5:
        valoracion="no,aprobado"
    return valoracion

print(evaluacion(notas))

#######utilizando in para ver que si crelegida esta en careras
careras = ["ingeniero", "programador", "docente","tutor"]
print("escoga la  carrera que desee: ingeniro, programdor, docente, tutor ")
crelegida=input("dijite su carrera escogida: ")
# poniendo lo escriba  en minuscula, tambien esta upper()
crelegida=crelegida.lower()
if crelegida in careras:
    print("la carrera elegida es " + crelegida)
else:
    print("eligio una carrera que no esta en la listas")

###trabajo del instructor oscar ####################################333
######################taller des profesor oscar 1:
nombre = input("dijite su  nombre: ")
mensualidad = int(input("dijite su  mensualidad: "))
edad = int(input("dijite su  edad: "))
sexo = input("dijite su sexo M o F: ")
sexo = sexo.upper()

if sexo == "M" and mensualidad < 1200000:
    print("usted " + nombre + " se encuentra en la categoria #a ")

elif sexo == "F" and mensualidad > 4000000:
    print("usted "+ nombre + " se encuentra en la categoria #b")

elif sexo == "F" and edad > 20 or edad < 30 and mensualidad > 1200000 or mensualidad < 4000000:
    print("usted "+ nombre + " se encuentra en la categoria #c")


#################ejercico numero 2
ingresos = int(input("por favor dijite su ingresos: "))
estado_civil = input("dijite S si esta soltero o C si esta casado: ")
estado_civil = estado_civil.upper()
tiene_hijos = input("dijite si tien hijos escreiba SI o NO: ")
tiene_hijos = tiene_hijos.upper()


print(estado_civil)
if ingresos > 20000000:
    print("el credito se cosede")
elif ingresos < 20000000 or ingresos > 12000000 and estado_civil == "S":
    print("se consede el prestamo")
if ingresos > 15000000 or ingresos < 20000000 and estado_civil == "s" and tiene_hijos == "SI":
    print("se le consede el prestamo")
else:
    print("lo siento el prestamo no se le cosede")


# ####################ejercicio numero 5

horas_trabajadas = int(input("digite la cantidad de horas que trabaja: "))
pago_hora = float(input("digite el pago por cada hora: "))

if horas_trabajadas > 48:
    triple = horas_trabajadas-48
    sueldo = 40*pago_hora+(8*pago_hora*2)+(triple*pago_hora*3)
elif horas_trabajadas > 10:
    doble = horas_trabajadas-40
    sueldo = 40*pago_hora+(doble*pago_hora*2)
else:
    sueldo = horas_trabajadas*pago_hora
print("el sueldo total por las", horas_trabajadas,
      "horas trabajadas es: $", sueldo)
