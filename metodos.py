# ################################################### metodos python #########################################################
nombre = "aDrIaN"
# pone los nombre minusculas
nombre = nombre.lower()
# pone los nombre en m mayuscula
nombre = nombre.upper()
# cuanta cuantas vese esta la "a" en adrian
nombre.count("a")
print(nombre)


################################## metodos en lista################################
lista = [2, 7, 8, 14, 8]
# cuenta cuantos caracteres tien mi lista en
catidaenlalista = len(lista)
# busca el elemento mas mas alto de la  lista de
print(max(lista))
# busca el numero mas pequeño de la  lista
print(min(lista))
###############################ahñadir####################
# agregar elementos a mi lista de
lista.append("adrian")
#agregando listas dentro de lista
lista.append([12,23,"jimenez"])
#agregando los numero del 1 al 9 en la lista y los pone de ultimos
lista.extend(range(1,10))
#me permite agregar varios objetos a la lista como tal no dentro de nada
lista.extend([100,101,1002])
#agrega un objeto en la pocicion que tu le des, y lo que quieres agregar
lista.insert(1,100000)
################################eliminar####################
#elimina el numero que le indiques
lista.remove("adrian")
# ordenas los datos  de la lista de
ordenenlalista = lista.sort()
# ver los elementos de la lista alreves
alreverlista = lista.reverse()

print(lista)