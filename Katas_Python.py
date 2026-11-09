#PROYECTO LÓGICA: Katas de Python

# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias
# de cada letra en la cadena. Los espacios no deben ser considerados.
def contar_frecuencias(cadena):
    #se define un diccionario vacio llamado frecuencias dónde se guardarán las letras y el resultado de contarlas
    frecuencias = {}
    # se recorre la cadena introducida como parámetro a la función 
    for caracter in cadena:
        #si el caracter leido es distinto de un espacio en blanco 
        if caracter != " ":
            #el diccionario se compone de clave que es el caracter y el valor que es las veces que aparece 
            #devuelve el valor actual de la letra o 0 si todavía no existe en el diccionario.
            #si el caracter validado ya está en el diccionario sumamos 1
            frecuencias[caracter] = frecuencias.get(caracter, 0) + 1
    return frecuencias

texto = "contar frecuencias de cada letra"
resultado = contar_frecuencias(texto)
print(resultado)  # Resultado: {'c': 4, 'o': 1, 'n': 2, 't': 2, 'a': 5, 'r': 3, 'f': 1, 'e': 4, 'u': 1, 'i': 1, 's': 1, 'd': 2, 'l': 1}


#-------------------------------------------------------

# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()
# Función que devuelve el doble de un número
def doble(x):
    return x * 2

# Lista de números inicial
numeros = [3, 5, 7, 9, 11]

# map() : aplica la función doble a cada elemento de la lista
dobles = list(map(doble, numeros))

# Mostrar resultado
print(dobles) #resultado :[6, 10, 14, 18, 22]

#-------------------------------------------------------
#3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
#devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

# Función que busca las palabras que contienen la palabra objetivo
def buscar_palabras(lista_palabras, palabra_objetivo):

    # Lista donde se almacenarán las palabras que coincidan
    coincidencias = []

    # Recorrer cada palabra de la lista
    for palabra in lista_palabras:

        # Comprobar si la palabra objetivo está contenida en la palabra actual
        if palabra_objetivo in palabra:

            # Añadir la palabra a la lista de coincidencias
            coincidencias.append(palabra)

    # Devolver la lista de palabras encontradas
    return coincidencias


# Lista de palabras de ejemplo
palabras = ["perro", "arbol", "television", "ordenador", "puerta" ,"perroflauta"]

# Palabra que queremos buscar
objetivo = "perro"

# Llamar a la función y guardar el resultado
resultado = buscar_palabras(palabras, objetivo)

# Mostrar las palabras que contienen la palabra objetivo
print(resultado) #resultado : ['perro', 'perroflauta']

#-------------------------------------------------------

#4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()
# Función que calcula la diferencia entre los valores de dos listas
def diferencia_listas(lista1, lista2):

    # map() aplica la resta elemento a elemento:
    # primer elemento de lista1 - primer elemento de lista2, etc.
    diferencia = list(map(lambda x, y: x - y, lista1, lista2))

    # Devuelve la nueva lista con las diferencias
    return diferencia


# Listas de ejemplo
lista1 = [100, 201, 302, 40]
lista2 = [1, 2, 3, 4]

# Llamar a la función
resultado = diferencia_listas(lista1, lista2)

# Mostrar el resultado
print(resultado)  #resultado :[99, 199, 299, 36]

#-------------------------------------------------------------------
#5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
#defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
#que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
#una tupla que contenga la media y el estado.

# Función que calcula la media de una lista de números
# y determina si está aprobada o suspendida
def calcular_resultado(notas, nota_aprobado=5):

    # Calcular la media de las notas
    media = sum(notas) / len(notas)

    # Comprobar si la media es mayor o igual que la nota de aprobado
    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"

    # Devolver una tupla con la media y el estado
    return (media, estado)


# Lista de notas de ejemplo
notas = [6, 7, 5, 8, 4]

# Llamar a la función
resultado = calcular_resultado(notas)

# Mostrar el resultado
print(resultado) #Resultado : (6.0, 'aprobado') 


#------------------------------------------------------
#6. Escribe una función que calcule el factorial de un número de manera recursiva.
# Función recursiva que calcula el factorial de un número
def factorial(n):

    # Caso base: el factorial de 0 y 1 es 1
    if n == 0 or n == 1:
        return 1

    # Caso recursivo: n * factorial de (n - 1)
    return n * factorial(n - 1)


# Número de ejemplo
numero = 5

# Calcular el factorial
resultado = factorial(numero)

# Mostrar el resultado
print(resultado)  #resultado :120

#------------------------------------------------------------------------
#7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

# Función que convierte una lista de tuplas en una lista de cadenas
def tuplas_a_strings(lista_tuplas):

    # map() aplica la función str() a cada tupla de la lista
    lista_strings = list(map(str, lista_tuplas))

    # Devuelve la lista de cadenas
    return lista_strings


# Lista de tuplas de ejemplo
tuplas = [(11, 23), (13, 4), (57, 76)]

# Llamar a la función
resultado = tuplas_a_strings(tuplas)

# Mostrar el resultado
print(resultado) #resultado :['(11, 23)', '(13, 4)', '(57, 76)']

#----------------------------------------------------------------------
#8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
#o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
#indicando si la división fue exitosa o no.

# Programa que pide dos números al usuario y realiza una división
try:
    
    # Solicitar los números al usuario
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    
    # Realizar la división
    resultado = num1 / num2
    
    # Mostrar el resultado
    print("El resultado de la división es:", resultado)
    print("La división se realizó correctamente.")

# Manejar el error cuando se introduce un valor no numérico
except ValueError:
    print("Error: Debes introducir valores numéricos.")
    print("La división no pudo realizarse.")

# Manejar el error cuando se intenta dividir entre cero
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
    print("La división no pudo realizarse.")

    #resultado ---Introduce el primer número: 4
                #Introduce el segundo número: 3
                #El resultado de la división es: 1.3333333333333333
                #La división se realizó correctamente.

#--------------------------------------------------------------------
#9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
#excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
#"Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()
# Función que elimina las mascotas prohibidas de una lista
def filtrar_mascotas(lista_mascotas):

    # Lista de mascotas prohibidas
    mascotas_prohibidas = [
        "Mapache",
        "Tigre",
        "Serpiente Pitón",
        "Cocodrilo",
        "Oso"
    ]

    # filter() selecciona solo las mascotas que NO están prohibidas
    mascotas_permitidas = list(
        filter(
            lambda mascota: mascota not in mascotas_prohibidas,
            lista_mascotas
        )
    )

    # Devolver la nueva lista filtrada
    return mascotas_permitidas


# Lista de mascotas de ejemplo
mascotas = [
    "Perro",
    "Gato",
    "Mapache",
    "Loro",
    "Tigre",
    "Conejo",
    "Oso"
]

# Llamar a la función
resultado = filtrar_mascotas(mascotas)

# Mostrar el resultado
print(resultado)  #resultado:['Perro', 'Gato', 'Loro', 'Conejo']

#---------------------------------------------------------------
#10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
#excepción personalizada y maneja el error adecuadamente.
# Excepción personalizada para indicar que la lista está vacía
class ListaVaciaError(Exception):
    pass


# Función que calcula el promedio de una lista de números
def calcular_promedio(lista_numeros):

    # Comprobar si la lista está vacía
    if not lista_numeros:
        raise ListaVaciaError("No se puede calcular el promedio de una lista vacía.")

    # Calcular el promedio
    promedio = sum(lista_numeros) / len(lista_numeros)

    # Devolver el promedio
    return promedio


try:
    # Lista de ejemplo
    numeros = []

    # Llamar a la función
    resultado = calcular_promedio(numeros)

    # Mostrar el promedio si no hay errores
    print("El promedio es:", resultado)

# Manejar la excepción personalizada
except ListaVaciaError as error:
    print("Error:", error)


#-----------------------------------------------------------------
#11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
#valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones
#adecuadamente.
# Programa que solicita la edad al usuario y controla posibles errores

try:

    # Pedir la edad al usuario
    edad = int(input("Introduce tu edad: "))

    # Comprobar que la edad está dentro del rango permitido
    if edad < 0 or edad > 120:
        raise ValueError("La edad debe estar entre 0 y 120 años.")

    # Mostrar la edad si es correcta
    print("Edad válida:", edad)

# Manejar el error cuando el usuario introduce un valor no numérico
except ValueError as error:
    print("Error:", error)

# Mensaje que se muestra siempre al finalizar
finally:
    print("Fin del programa.")


#-----------------------------------------------------------
#12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()
# Función que recibe una frase y devuelve una lista
# con la longitud de cada palabra usando map()
def longitud_palabras(frase):

    # Dividir la frase en una lista de palabras
    palabras = frase.split()

    # Aplicar len() a cada palabra mediante map()
    longitudes = list(map(len, palabras))

    # Devolver la lista de longitudes
    return longitudes


# Frase de ejemplo
frase = "Python es un lenguaje muy potente"

# Llamar a la función
resultado = longitud_palabras(frase)

# Mostrar el resultado
print(resultado)   #resultado:# Función que recibe una frase y devuelve una lista
# con la longitud de cada palabra usando map()
def longitud_palabras(frase):

    # Dividir la frase en una lista de palabras
    palabras = frase.split()

    # Aplicar len() a cada palabra mediante map()
    longitudes = list(map(len, palabras))

    # Devolver la lista de longitudes
    return longitudes


# Frase de ejemplo
frase = "Python es un lenguaje muy potente"

# Llamar a la función
resultado = longitud_palabras(frase)

# Mostrar el resultado
print(resultado)  #resultado:# Función que recibe una frase y devuelve una lista
# con la longitud de cada palabra usando map()
def longitud_palabras(frase):

    # Dividir la frase en una lista de palabras
    palabras = frase.split()

    # Aplicar len() a cada palabra mediante map()
    longitudes = list(map(len, palabras))

    # Devolver la lista de longitudes
    return longitudes


# Frase de ejemplo
frase = "Python es un lenguaje muy potente"

# Llamar a la función
resultado = longitud_palabras(frase)

# Mostrar el resultado
print(resultado)  #resultado:[6, 2, 2, 8, 3, 6]


#-----------------------------------------------------
#13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
#mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()
# Función que recibe un conjunto de caracteres y devuelve
# una lista de tuplas con cada letra en mayúsculas y minúsculas
def convertir_letras(conjunto_letras):

    # map() aplica una función a cada letra del conjunto
    # y genera una tupla (mayúscula, minúscula)
    resultado = list(
        map(
            lambda letra: (letra.upper(), letra.lower()),
            conjunto_letras
        )
    )

    # Devolver la lista de tuplas
    return resultado


# Conjunto de letras de ejemplo (no admite repetidos)
letras = {"a", "b", "c", "d"}

# Llamar a la función
lista_tuplas = convertir_letras(letras)

# Mostrar el resultado
print(lista_tuplas) #resultado:[('A', 'a'), ('B', 'b'), ('C', 'c'), ('D', 'd')]

#--------------------------------------------------------------------
#14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()
# Función que devuelve las palabras que comienzan
# por una letra específica usando filter()
def filtrar_por_letra(lista_palabras, letra):

    # filter() selecciona únicamente las palabras
    # que empiezan por la letra indicada
    resultado = list(
        filter(
            lambda palabra: palabra.startswith(letra),
            lista_palabras
        )
    )

    # Devolver la lista filtrada
    return resultado


# Lista de palabras de ejemplo
palabras = ["casa", "coche", "perro", "camino", "gato", "cometa"]

# Letra por la que deben comenzar las palabras
letra = "c"

# Llamar a la función
resultado = filtrar_por_letra(palabras, letra)

# Mostrar el resultado
print(resultado)  #resultado:['casa', 'coche', 'camino', 'cometa']

#------------------------------------------------------------------
#15. Crea una función lambda que sume 3 a cada número de una lista dada.
# Lista de números de ejemplo
numeros = [2, 5, 8, 10]

# Usar una función lambda junto con map()
# para sumar 3 a cada elemento de la lista
resultado = list(map(lambda x: x + 3, numeros))

# Mostrar el resultado
print(resultado)  #resultado:[5, 8, 11, 13]


#--------------------------------------------------------------------
#16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
#todas las palabras que sean más largas que n. Usa la función filter()
# Función que devuelve las palabras de una frase
# cuya longitud es mayor que el valor n
def palabras_largas(frase, n):

    # Convertir la frase en una lista de palabras
    palabras = frase.split()

    # Filtrar las palabras que tengan más de n caracteres
    resultado = list(
        filter(
            lambda palabra: len(palabra) > n,
            palabras
        )
    )

    # Devolver la lista filtrada
    return resultado 

# Frase de ejemplo
texto = "Python es un lenguaje de programación muy potente"

# Longitud mínima
n = 5

# Llamar a la función
resultado = palabras_largas(texto, n)

# Mostrar el resultado
print(resultado) #resultado:['Python', 'lenguaje', 'programación', 'potente']

#----------------------------------------------------------------------
#17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
#corresponde al número quinientos setenta y dos (572). Usa la función reduce()

from functools import reduce

# Función que convierte una lista de dígitos en un número
def lista_a_numero(lista_digitos):

    # reduce() va construyendo el número dígito a dígito
    numero = reduce(
        lambda acumulador, digito: acumulador * 10 + digito,
        lista_digitos
    )

    # Devolver el número resultante
    return numero


# Lista de dígitos de ejemplo
digitos = [5, 7, 2]

# Llamar a la función
resultado = lista_a_numero(digitos)

# Mostrar el resultado
print(resultado)  #resultado:572

#--------------------------------------------------------------------------
#18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
#(nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a
# 90. Usa la función filter()

# Lista de diccionarios con información de estudiantes
estudiantes = [
    {"nombre": "Ana", "edad": 18, "calificacion": 95},
    {"nombre": "Luis", "edad": 19, "calificacion": 85},
    {"nombre": "Marta", "edad": 20, "calificacion": 92},
    {"nombre": "Pedro", "edad": 18, "calificacion": 78},
    {"nombre": "Sofía", "edad": 21, "calificacion": 90}
]

# Usar filter() para obtener los estudiantes
# con una calificación mayor o igual a 90
estudiantes_destacados = list(
    filter(
        lambda estudiante: estudiante["calificacion"] >= 90,
        estudiantes
    )
)

# Mostrar los estudiantes filtrados
print(estudiantes_destacados) 
#resultado :
#[
#    {'nombre': 'Ana', 'edad': 18, 'calificacion': 95},
#    {'nombre': 'Marta', 'edad': 20, 'calificacion': 92},
#    {'nombre': 'Sofía', 'edad': 21, 'calificacion': 90}
#]

#--------------------------------------------------------------------------
#19. Crea una función lambda que filtre los números impares de una lista dada
# Lista de números de ejemplo
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Función lambda que selecciona únicamente
# los números impares de la lista
impares = list(filter(lambda x: x % 2 != 0, numeros))

# Mostrar el resultado
print(impares)  #resultado:[1, 3, 5, 7, 9]

#------------------------------------------------------------------------------
#20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función
#filter()
# Lista con elementos de tipo entero (int) y cadena (str)
datos = [10, "hola", 25, "Python", 40, "mundo", 7]

# filter() selecciona únicamente los elementos
# que son de tipo entero
solo_enteros = list(
    filter(
        lambda elemento: isinstance(elemento, int),
        datos
    )
)

# Mostrar el resultado
print(solo_enteros) #resultado:[10, 25, 40, 7]

#-------------------------------------------------------------
#21. Crea una función que calcule el cubo de un número dado mediante una función lambda
# Función lambda que calcula el cubo de un número
cubo = lambda x: x ** 3

# Número de ejemplo
numero = 4

# Calcular el cubo del número
resultado = cubo(numero)

# Mostrar el resultado
print(resultado) #resultado: 64

#------------------------------------------------------------------------
#22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .
from functools import reduce

# Función que calcula el producto de todos los números de una lista
def producto_total(lista_numeros):

    # reduce() multiplica todos los elementos de la lista
    producto = reduce(
        lambda x, y: x * y,
        lista_numeros
    )

    # Devolver el resultado
    return producto


# Lista de números de ejemplo
numeros = [2, 3, 4, 5]

# Llamar a la función
resultado = producto_total(numeros)

# Mostrar el resultado
print(resultado) #resultado:120

#--------------------------------------------------------------
#23. Concatena una lista de palabras.Usa la función reduce() .
from functools import reduce

# Función que concatena una lista de palabras
def concatenar_palabras(lista_palabras):

    # reduce() une todas las palabras de la lista
    frase = reduce(
        lambda x, y: x + " " + y,
        lista_palabras
    )

    # Devolver la cadena resultante
    return frase


# Lista de palabras de ejemplo
palabras = ["Vive", "feliz", "la", "vida"]

# Llamar a la función
resultado = concatenar_palabras(palabras)

# Mostrar el resultado
print(resultado) #resultado:Vive feliz la vida


#-------------------------------------------------------
#24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .
from functools import reduce

# Función que calcula la diferencia total de los valores de una lista
def diferencia_total(lista_numeros):

    # reduce() va restando cada elemento al acumulador
    diferencia = reduce(
        lambda x, y: x - y,
        lista_numeros
    )

    # Devolver el resultado
    return diferencia


# Lista de números de ejemplo
numeros = [100, 20, 10, 5]

# Llamar a la función
resultado = diferencia_total(numeros)

# Mostrar el resultado
print(resultado)  #resultado:65

#---------------------------------------------------------------------
#25. Crea una función que cuente el número de caracteres en una cadena de texto dada.
# Función que cuenta el número de caracteres de una cadena
def contar_caracteres(texto):

    # Obtener la longitud de la cadena
    cantidad = len(texto)

    # Devolver la cantidad de caracteres
    return cantidad


# Cadena de texto de ejemplo
frase = "Hola mundo"

# Llamar a la función
resultado = contar_caracteres(frase)

# Mostrar el resultado
print("Número de caracteres:", resultado)  #resultado:Número de caracteres: 10

#-----------------------------------------------------------------------
#26. Crea una función lambda que calcule el resto de la división entre dos números dados.
# Función lambda que calcula el resto de una división
resto = lambda x, y: x % y

# Números de ejemplo
a = 17
b = 5

# Calcular el resto de la división
resultado = resto(a, b)

# Mostrar el resultado
print(resultado) #resultado:2

#------------------------------------------------------------------------
#27. Crea una función que calcule el promedio de una lista de números.
# Función que calcula el promedio de una lista de números
def calcular_promedio(lista_numeros):

    # Calcular la suma de todos los números
    suma = sum(lista_numeros)

    # Calcular la cantidad de elementos de la lista
    cantidad = len(lista_numeros)

    # Calcular el promedio
    promedio = suma / cantidad

    # Devolver el promedio
    return promedio


# Lista de números de ejemplo
numeros = [10, 8, 6, 4]

# Llamar a la función
resultado = calcular_promedio(numeros)

# Mostrar el resultado
print("El promedio es:", resultado)  #resultado:El promedio es: 7.0

#-------------------------------------------------------------------------
#28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
# Función que busca y devuelve el primer elemento duplicado de una lista
def primer_duplicado(lista):

    # Conjunto para guardar los elementos ya vistos
    vistos = set()
    # Recorrer los elementos de la lista
    for elemento in lista:

        # Si el elemento ya ha aparecido antes, es un duplicado
        if elemento in vistos:
            return elemento

        # Añadir el elemento al conjunto de vistos
        vistos.add(elemento)

    # Si no hay elementos duplicados, devolver None
    return None
# Lista de ejemplo
numeros = [4, 7, 2, 9, 7, 5, 2]

# Llamar a la función
resultado = primer_duplicado(numeros)

# Mostrar el resultado
print("Primer elemento duplicado:", resultado) #resultado:Primer elemento duplicado: 7


#--------------------------------------------------------------------------
#29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
#carácter '#', excepto los últimos cuatro.
# Función que convierte cualquier valor en una cadena
# y oculta todos los caracteres excepto los últimos 4
def enmascarar(valor):

    # Convertir el valor a cadena de texto
    texto = str(valor)

    # Si la longitud es menor o igual a 4,
    # se devuelve la cadena sin modificar
    if len(texto) <= 4:
        return texto

    # Reemplazar todos los caracteres excepto los últimos 4 por '#'
    return "#" * (len(texto) - 4) + texto[-4:]


# Ejemplos de uso
print(enmascarar("123456789"))
print(enmascarar(987654321))
print(enmascarar("ABCD1234")) 

#resultado: 
######6789
#####4321
####1234 


#------------------------------------------------------
#30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
#pero en diferente orden.
# Función que determina si dos palabras son anagramas
def son_anagramas(palabra1, palabra2):

    # Convertir las palabras a minúsculas
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()

    # Ordenar las letras y compararlas
    return sorted(palabra1) == sorted(palabra2)


# Ejemplos de uso
print(son_anagramas("roma", "amor"))
print(son_anagramas("listen", "silent"))
print(son_anagramas("casa", "saco")) 

#resultado:
#True
#True
#False

#---------------------------------------------------------
#31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
#esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
#lanza una excepción.

# Excepción personalizada para cuando el nombre no se encuentra
class NombreNoEncontradoError(Exception):
    pass


# Función que solicita una lista de nombres y busca un nombre específico
def buscar_nombre():

    try:
        # Pedir al usuario los nombres separados por comas
        entrada = input("Introduce una lista de nombres separados por comas: ")

        # Convertir la entrada en una lista
        nombres = entrada.split(",")

        # Eliminar espacios en blanco al principio y final de cada nombre
        nombres = [nombre.strip() for nombre in nombres]

        # Pedir el nombre que se desea buscar
        nombre_buscar = input("Introduce el nombre que deseas buscar: ")

        # Comprobar si el nombre está en la lista
        if nombre_buscar in nombres:
            print("Nombre encontrado en la lista.")
        else:
            # Lanzar una excepción si el nombre no existe
            raise NombreNoEncontradoError(
                f"El nombre '{nombre_buscar}' no se encuentra en la lista."
            )

    # Manejar la excepción personalizada
    except NombreNoEncontradoError as error:
        print("Error:", error)


# Llamar a la función
buscar_nombre()


#------------------------------------------------------------
#32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
#devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
#no trabaja aquí.

# Función que busca un empleado por su nombre completo
# y devuelve su puesto de trabajo
def buscar_empleado(nombre_completo, lista_empleados):

    # Recorrer la lista de empleados
    for empleado in lista_empleados:

        # Comprobar si el nombre coincide
        if empleado["nombre"] == nombre_completo:
            return empleado["puesto"]

    # Si no se encuentra el empleado
    return "La persona no trabaja aquí."


# Lista de empleados
empleados = [
    {"nombre": "Ana García", "puesto": "Administrativa"},
    {"nombre": "Luis Pérez", "puesto": "Programador"},
    {"nombre": "Marta López", "puesto": "Diseñadora"},
    {"nombre": "Pedro Ruiz", "puesto": "Contable"}
]

# Buscar un empleado
resultado = buscar_empleado("Luis Pérez", empleados)

# Mostrar el resultado
print(resultado)

#-----------------------------------------------------------------
#33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.
# Listas de ejemplo
lista1 = [1, 2, 3, 4]
lista2 = [10, 20, 30, 40]

# Función lambda que suma los elementos correspondientes
# de las dos listas usando map()
resultado = list(map(lambda x, y: x + y, lista1, lista2))

# Mostrar el resultado
print(resultado) #resultado:[11, 22, 33, 44] 


#-------------------------------------------------------------------
#34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
#crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
#manipular la estructura del árbol.
#Código a seguir:
#1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
#2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
#3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
#4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
#5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
#6. Implementar el método
#info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las
#mismas.
#Caso de uso:
#1. Crear un árbol.
#2. Hacer crecer el tronco del árbol una unidad.
#3. Añadir una nueva rama al árbol.
#4. Hacer crecer todas las ramas del árbol una unidad.
#5. Añadir dos nuevas ramas al árbol.
#6. Retirar la rama situada en la posición 2.
#7. Obtener información sobre el árbol.

# Clase que representa un árbol
class Arbol:

    # Constructor: inicializa el tronco y la lista de ramas
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    # Aumenta la longitud del tronco en una unidad
    def crecer_tronco(self):
        self.tronco += 1

    # Añade una nueva rama de longitud 1
    def nueva_rama(self):
        self.ramas.append(1)

    # Aumenta en una unidad la longitud de todas las ramas
    def crecer_ramas(self):
        for i in range(len(self.ramas)):
            self.ramas[i] += 1

    # Elimina una rama según su posición
    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)

    # Devuelve información sobre el árbol
    def info_arbol(self):
        return {
            "Longitud del tronco": self.tronco,
            "Número de ramas": len(self.ramas),
            "Longitudes de las ramas": self.ramas
        }


# -------------------------
# Caso de uso
# -------------------------

# 1. Crear un árbol
arbol = Arbol()

# 2. Hacer crecer el tronco una unidad
arbol.crecer_tronco()

# 3. Añadir una nueva rama
arbol.nueva_rama()

# 4. Hacer crecer todas las ramas una unidad
arbol.crecer_ramas()

# 5. Añadir dos nuevas ramas
arbol.nueva_rama()
arbol.nueva_rama()

# 6. Retirar la rama situada en la posición 2
arbol.quitar_rama(2)

# 7. Obtener información del árbol
info = arbol.info_arbol()

# Mostrar la información
print(info)

#resultado : {
 #   'Longitud del tronco': 2,
#  'Número de ramas': 2,
 #   'Longitudes de las ramas': [2, 1]
#}

#--------------------------------------------------------------------
'''
36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
agregar dinero al saldo.
Código a seguir:
1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no
poder hacerse.
3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual.
Lanzará un error en caso de no poder hacerse.
4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
Caso de uso:
1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
2. Agregar 20 unidades de saldo de "Bob".
3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
4. Retirar 50 unidades de saldo a "Alicia".

'''
# Clase que representa a un usuario de un banco
class UsuarioBanco:

    # Constructor: inicializa el nombre, saldo y si tiene cuenta corriente
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    # Método para retirar dinero de la cuenta
    def retirar_dinero(self, cantidad):

        # Comprueba si el usuario tiene cuenta corriente
        if not self.cuenta_corriente:
            raise Exception(f"{self.nombre} no tiene cuenta corriente.")

        # Comprueba si tiene saldo suficiente
        if cantidad > self.saldo:
            raise Exception(f"Saldo insuficiente para {self.nombre}.")

        # Resta la cantidad al saldo
        self.saldo -= cantidad

        # Muestra un mensaje de confirmación
        print(f"{self.nombre} ha retirado {cantidad} €. Saldo actual: {self.saldo} €")

    # Método para recibir una transferencia desde otro usuario
    def transferir_dinero(self, otro_usuario, cantidad):

        # Comprueba que ambos usuarios tienen cuenta corriente
        if not self.cuenta_corriente:
            raise Exception(f"{self.nombre} no tiene cuenta corriente.")

        if not otro_usuario.cuenta_corriente:
            raise Exception(f"{otro_usuario.nombre} no tiene cuenta corriente.")

        # Comprueba que el usuario que envía el dinero tiene saldo suficiente
        if otro_usuario.saldo < cantidad:
            raise Exception(
                f"{otro_usuario.nombre} no tiene saldo suficiente para la transferencia."
            )

        # Resta el dinero al usuario que envía
        otro_usuario.saldo -= cantidad

        # Suma el dinero al usuario que recibe
        self.saldo += cantidad

        # Muestra un mensaje informativo
        print(f"{otro_usuario.nombre} ha transferido {cantidad} € a {self.nombre}")

    # Método para ingresar dinero en la cuenta
    def agregar_dinero(self, cantidad):

        # Añade la cantidad al saldo
        self.saldo += cantidad

        # Muestra el nuevo saldo
        print(
            f"Se han añadido {cantidad} € a la cuenta de {self.nombre}. "
            f"Saldo actual: {self.saldo} €"
        )
        # ==========================
# CASO DE USO
# ==========================

# Crear usuario Alicia con 100 € y cuenta corriente
alicia = UsuarioBanco("Alicia", 100, True)

# Crear usuario Bob con 50 € y cuenta corriente
bob = UsuarioBanco("Bob", 50, True)

# Añadir 20 € a Bob
bob.agregar_dinero(20)

# Transferir 80 € desde Bob a Alicia
alicia.transferir_dinero(bob, 80)

# Retirar 50 € de la cuenta de Alicia
alicia.retirar_dinero(50)

# Mostrar los saldos finales
print("\nSaldos finales:")
print(f"Alicia: {alicia.saldo} €")
print(f"Bob: {bob.saldo} €")


#---------------------------------------------
'''
37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras ,
reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
de la función procesar_texto .
Código a seguir:
1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene
que devolver un diccionario.
2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene
que devolver el texto con el remplazo de palabras.
3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra
eliminada.
4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un
número de argumentos variable según la opción indicada.
Caso de uso:
Comprueba el funcionamiento completo de la función procesar_texto
'''
# Función principal que ejecuta una acción según la opción indicada
def procesar_texto(texto, opcion, *args):

    # Opción para contar palabras
    if opcion == "contar":
        return contar_palabras(texto)

    # Opción para reemplazar palabras
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, *args)

    # Opción para eliminar palabras
    elif opcion == "eliminar":
        return eliminar_palabra(texto, *args)

    # Control de errores si la opción no existe
    else:
        return "Opción no válida"


# --------------------------
# PRUEBAS DEL PROGRAMA
# --------------------------

# Texto de ejemplo
texto = "Ejercicio de contar palabras en un texto"

# Contar palabras
print("Contar palabras:")
print(procesar_texto(texto, "contar"))

# Reemplazar una palabra por otra
print("\nReemplazar palabras:")
print(procesar_texto(texto, "reemplazar", "Ejercicio", "Prueba"))

# Eliminar una palabra
print("\nEliminar palabra:")
print(procesar_texto(texto, "eliminar", "texto"))

#-----------------------------------------------------------
#38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
# Solicitar al usuario que introduzca una hora en formato de 24 horas
# (por ejemplo: 8, 15 o 22)
hora = int(input("Introduce la hora (0-23): "))

# Comprobar si la hora corresponde a la mañana
# Desde las 06:00 hasta las 11:59
if 6 <= hora < 12:
    print("Es de día (mañana).")

# Comprobar si la hora corresponde a la tarde
# Desde las 12:00 hasta las 19:59
elif 12 <= hora < 20:
    print("Es de tarde.")

# Comprobar si la hora corresponde a la noche
# Desde las 20:00 hasta las 23:59 y desde las 00:00 hasta las 05:59
elif 0 <= hora < 24:
    print("Es de noche.")

# Si la hora está fuera del rango 0-23, mostrar un mensaje de error
else:
    print("La hora introducida no es válida.")


#----------------------------------------------------------------------------------------
'''
39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
Las reglas de calificación son:
- 0 - 69 insuficiente
- 70 - 79 bien
- 80 - 89 muy bien
- 90 - 100 excelente
'''
# Solicitar al usuario que introduzca una calificación numérica
nota = int(input("Introduce la calificación (0-100): "))

# Comprobar si la nota está entre 0 y 69
if 0 <= nota <= 69:
    print("Insuficiente")

# Comprobar si la nota está entre 70 y 79
elif 70 <= nota <= 79:
    print("Bien")

# Comprobar si la nota está entre 80 y 89
elif 80 <= nota <= 89:
    print("Muy bien")

# Comprobar si la nota está entre 90 y 100
elif 90 <= nota <= 100:
    print("Excelente")

# Mostrar un mensaje de error si la nota está fuera del rango válido
else:
    print("La calificación introducida no es válida.")


#--------------------------------------------------------
#40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o
#"triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).

import math

# Función que calcula el área de una figura geométrica
def calcular_area(figura, datos):

    # Calcular el área de un rectángulo
    # datos = (base, altura)
    if figura.lower() == "rectangulo":
        base, altura = datos
        return base * altura

    # Calcular el área de un círculo
    # datos = (radio,)
    elif figura.lower() == "circulo":
        radio = datos[0]
        return math.pi * radio**2

    # Calcular el área de un triángulo
    # datos = (base, altura)
    elif figura.lower() == "triangulo":
        base, altura = datos
        return (base * altura) / 2

    # Mensaje si la figura no es válida
    else:
        return "Figura no válida"


# -------------------------
# PRUEBAS DEL PROGRAMA
# -------------------------

# Área de un rectángulo de base 5 y altura 3
print("Rectángulo:", calcular_area("rectangulo", (5, 3)))

# Área de un círculo de radio 4
print("Círculo:", calcular_area("circulo", (4,)))

# Área de un triángulo de base 6 y altura 2
print("Triángulo:", calcular_area("triangulo", (6, 2)))

#--------------------------------------------------------------
'''
41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo
siguiente:
1. Solicita al usuario que ingrese el precio original de un artículo.
2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor
a cero). Por ejemplo, descuento de 15€.
5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu
programa de Python.
'''
# Solicitar al usuario el precio original del artículo
precio_original = float(input("Introduce el precio del artículo: "))

# Preguntar al usuario si dispone de un cupón de descuento
cupon = input("¿Tienes un cupón de descuento? (si/no): ").lower()

# Comprobar si el usuario tiene cupón
if cupon == "si":

    # Solicitar el valor del descuento
    descuento = float(input("Introduce el valor del cupón (€): "))

    # Verificar que el descuento sea mayor que 0
    if descuento > 0:

        # Calcular el precio final aplicando el descuento
        precio_final = precio_original - descuento

        # Evitar que el precio final sea negativo
        if precio_final < 0:
            precio_final = 0

        # Mostrar el precio final
        print(f"El precio final es: {precio_final:.2f} €")

    else:
        # Mensaje si el valor del cupón no es válido
        print("El valor del cupón no es válido.")
        print(f"El precio final es: {precio_original:.2f} €")

# Si el usuario no tiene cupón
elif cupon == "no":

    # El precio final será el precio original
    print(f"El precio final es: {precio_original:.2f} €")

# Si la respuesta no es 'si' ni 'no'
else:
    print("Respuesta no válida. Debes escribir 'si' o 'no'.")