DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    ##cada persona##
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    ###con lis comprengenshion#######
    nombre_trabajadores = [cada_persona["name"]for cada_persona in DATA if cada_persona ['language'] == "python"]
    for cada_persona in nombre_trabajadores:
        print(f" esta persona sabe python {cada_persona}")


    ##utilizando listas de orden superior## hace me filta todo el dicionario de la persona###
    nombre_trabajadores = list(filter(lambda cada_persona: cada_persona ['language'] == 'python',DATA))
    ##filtrando el nombre de las personas de nombre_trabajadores#####33
    nombre_trabajadores = list(map(lambda cada_persona: cada_persona ["name"],nombre_trabajadores))
    for cada_persona in nombre_trabajadores:
        print(cada_persona)


    trabajoderesPlatzi = [cada_persona["name"]for cada_persona in DATA if cada_persona ['organization'] == 'Platzi']
    for  cada_persona in trabajoderesPlatzi:
        print(f" esta persona trabja en platzi {cada_persona}")


    #este codigo es un poco complejo, pero intenta leerlo y resultara facil #####
    personas_mayores_30 = list(filter(lambda cada_persona: cada_persona ["age"] > 30,DATA))
    personas_mayores_30 = list(map(lambda cada_persona: cada_persona ["name"],personas_mayores_30))
    for cada_persona in personas_mayores_30:
        print(f"esta persona es mayor a 30 años {cada_persona}")



    backen_developer = [cada_persona ["name"] for cada_persona in DATA if cada_persona ["position"] == 'Backend Developer']
    for cada_persona in backen_developer:
        print(f" esta persona sabe de backen_developer {cada_persona}")

    print(DATA["ASFRSD"])

if __name__ == '__main__':
    run()