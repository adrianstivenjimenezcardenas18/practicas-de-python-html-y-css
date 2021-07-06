def run():
    pass
####
nombre = input("dijite su nombre")
######################## funcion lambda, mirndo si un nombre se es igual alreves #########################
palindromo = lambda nombre: nombre == nombre[::-1]

print(palindromo(nombre))

###################################### funciones de order superio filter, map y reduce####################

######filter###########
my_list = [1,4,5,6,9,13,19,21]

numero_impares = list(filter(lambda x : x%2 != 0, my_list))
print(numero_impares)

####### map ############
my_list = [1,2,3,4,5]

numero_elev_cuadrado = list(map(lambda i : i**2, my_list))
print(numero_elev_cuadrado)

############### reduce ########
##importando funcion
from functools import reduce
my_list = [2,2,2,2,2]

numero_reducid = reduce(lambda a,b: a*b, my_list)


if __name__ == '__main__':
    run()