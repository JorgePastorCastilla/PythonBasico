# STRINGS
# Se usan para almacenar textos de informacion
# y se indican con comillas simples o dobles

cadena1 = "hola"
cadena2 = 'hola'
cadena3 = "esto es una prueba o 'prova'"

a = 5
b = 7
nombre1 = "Maria"
nombre2 = "Juan"

# utilizando el metodo format que se puede usar con los strings
print("{} tiene {} manzanas y {} tiene {} peras".format(nombre1,a,nombre2,b))
print("{a} manzana".format(a=nombre1))

# Imprimir por pantalla utilizando operadores
print(nombre1 + " tiene " + str(a) + " manzanas " + nombre2 + " tiene " + str(b) + " peras")

# Indexacion
cadena4 = "prueba"
print(cadena4[0])
print(cadena4[-1])
print(cadena4[2:])
print (cadena4[:3])
print(cadena4[2:3])
print(cadena4[::])
print(cadena4[::2])
print(cadena4[::1])
print("Prueba de cosas raras")
print(cadena4[-1:-len(cadena4)])
print("Fin de pruebas raras")


# cadena4[2] = "x" -> no se puede porque son inmutables
cadena4 = "adios"
print(cadena4)

# Metodos mas utilizados
print(cadena4.upper())
print(cadena4.lower())

cadena5 = "Belen"
print(cadena5.lower())

cadena6 = "esto es una prueba"
print(cadena6.capitalize())

# Segmentacion
print(cadena6.split())
print(cadena6.split('e'))