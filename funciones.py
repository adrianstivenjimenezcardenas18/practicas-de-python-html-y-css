# # funciones
# def mensaje():
#     print("hola mi nombre es adrian y estoy creando esta funcion")
#     print("tengo 18 años y estoy aprendiendo python")


# mensaje()

# # funciones con parametros


# def suma(numero1, numero2):
#     print(numero1+numero2)


# suma(5, 5)

# suma(10, 10)

# suma(10, 20)

# #### funcione
# nombre = input("dijite su nombre: ")
# apellido = input("dijite su apellido: ")


# def nombre_completo(nombre, apellido, inverso=False):
#     if inverso == True:
#         return print(f"{nombre} {apellido}")
#     else:
#         return print(f"{apellido} {nombre}")


# (nombre_completo(nombre, apellido, ))

###### definir lo que hace la funcion


def a(numero1, numero2):
    """ esta funcion suma dos numeros  y
    retorna el resultado"""
    total = numero1 + numero2
    return print(f" este es el resultado de la suma {total}")

a(2,2)

####para leer(en programcion llamado dostrin) lo que dice la funcion en por dentro
help(a)