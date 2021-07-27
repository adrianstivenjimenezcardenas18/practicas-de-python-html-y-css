# ################################# listas en python ejerccios
miLista = ["maria", "pepe", "marta", "antonio", ["adriann", 12, 34]]
# ingresando a un atupla dentro de otra tupla
print(miLista[4][0])
# imprimiendo el objeto marta de la lista
print(miLista[3])
# imprimiendo alrever la lita y imprimiendo antonio
print(miLista[-2])
# imprimiendo maria hasta el 3
print(miLista[0:3])
# imprimiendo de pepe hasta dond eacabe la lista
print(miLista[1:])
# cambiando un objeto por otro
miLista.insert(1, "adrian")
# te dice la  paccion de ese nombre
print(miLista.index("adrian"))
print(miLista)


####### clonar listas en python
a = ["adrian", 1, 2]
#asi se clona una lista
c = list(a)
#otra forma de clonar listas
d = a[::]
#mirando los id
print(id(a))
print(id(c))
print(id(d))


# ############################3 ejerccios de tupla
tupla = ("juan", 13, 1, 1995)
print(tupla[2])

tupla = ("juan", 13, 1, 1995)
# combertir tuplas en listas y viseversa con "tuple"
milista = list(tupla)
print(milista)
# imprimiendo si ese nombre o varable esta en en la lista tupla
print("juan" in milista)
# contar cuantas veses hay un avariable en la listas o tuplas
print(milista.count("juan"))
# contar cuantos caracteres tien en este caso mi listas
print(len(milista))

# #########################ejerccios de diccionario
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
