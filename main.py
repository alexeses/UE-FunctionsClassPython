def generar_n_caracteres(n, c):
    print("Ejercicio 1")
    print("El caracter " + c + " se repite " + str(n) + " veces ")
    return c * n

def histograma(lista_numeros):
    print("Ejercicio 2")
    for i in lista_numeros:
        print("*" * i)

def funcionLista(funcion, lista):
    print("Ejercicio 3")
    lista_nueva = []
    for i in lista:
        lista_nueva.append(funcion(i))
    return lista_nueva

def palabrasLongitud(frase):
    print("Ejercicio 4")
    diccionario = {}
    lista_palabras = frase.split(" ")
    for i in lista_palabras:
        diccionario[i] = len(i)
    return diccionario

def calificaPalabras(diccionario):
    print("Ejercicio 5")
    diccionario_nuevo = {}
    for i in diccionario:
        if diccionario[i] < 5:
            diccionario_nuevo[i.upper()] = "Suspenso"
        elif diccionario[i] >= 5 and diccionario[i] < 7:
            diccionario_nuevo[i.upper()] = "Aprobado"
        elif diccionario[i] >= 7 and diccionario[i] < 9:
            diccionario_nuevo[i.upper()] = "Notable"
        elif diccionario[i] >= 9 and diccionario[i] <= 10:
            diccionario_nuevo[i.upper()] = "Sobresaliente"
    return diccionario_nuevo


# use switch case 1 2 3
def switch_case():
    print("Seleccione una opcion:")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("4. Ejercicio 4")
    print("5. Ejercicio 5")
    print("0. Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 0:
        print("Good bye!")
        return
    if opcion == 1:
        n = int(input("Ingrese un numero: "))
        c = input("Ingrese un caracter: ")
        print(generar_n_caracteres(n, c))
    elif opcion == 2:
        lista_numeros = []
        n = int(input("Ingrese el total de numeros: "))
        for i in range(n):
            lista_numeros.append(int(input("Ingrese un numero el numero " + str(i + 1) + ": ")))
        histograma(lista_numeros)
    elif opcion == 3:
        lista_numeros = []
        n = int(input("Ingrese la cantidad de numeros: "))
        for i in range(n):
            lista_numeros.append(int(input("Ingrese un numero: ")))
        print(funcionLista(lambda x: x ** 3, lista_numeros))
    elif opcion == 4:
        print("Ingresa una frase: ")
        frase = input()
        print(palabrasLongitud(frase))
    elif opcion == 5:
        diccionario = {}
        n = int(input("Ingrese la cantidad de asignaturas: "))
        for i in range(n):
            diccionario[input("Ingrese el nombre de la asignatura: ")] = float(input("Ingrese la nota: "))
        print(calificaPalabras(diccionario))
    else:
        print("Opcion incorrecta")
        switch_case()

switch_case()
