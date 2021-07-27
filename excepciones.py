# # ejerccios de excepciones
# numero1 = int(input("dijite un numero 1: "))
# numero2 = int(input("dijite un numero 2: "))


# def divide(numero1, numero2):
#     # sirve por si ahy un error, siga corriendo el codigo normal
#     try:
#         return numero1 / numero2
#     except ZeroDivisionError:
#         print("lo sinto no se puede dividir por cero")


# print(divide(numero1, numero2))
# print("gracias por insertar los numeros")

# # ######


# def divide():
#     try:
#         op1 = float(input("introduce el primer numero: "))
#         op2 = float(input("introduce el segundo numero: "))
#         print("la divison es " + str(op1/op2))
#     except ValueError:
#         print("el valor introducido es erroneo")
#         # pone esto mas el nombre del ERROR que te da en la consola
#     except ZeroDivisionError:
#         print("no se puede dividir por cero")
#         # hacer qu esta linea se ejecute siempre con finally
#     finally:
#         print("calculo finalizado")

################excepciones de####################
def divide_elementos_de_lista(lista, divisor):
    try:
        return [i / divisor for i in lista]
        ## el as es para asignar el zeroDivisionError
    except ZeroDivisionError as e:
        #imprimame el error
        print(e)
        return listas


listas = list(range(10))

divisor = 0
print(divide_elementos_de_lista(listas, divisor))
