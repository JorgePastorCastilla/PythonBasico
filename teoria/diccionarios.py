#DICCIONARIOS#
""""
Son la version de Python de una matriz asociatiba
(hashtable)
Son un sistema de pares de valores clave
Se define con {}
"""
midiccionario = {"clave1":"valor1", "clave2":"valor2", "clave3":{"dentro":[1,2,3]}}
print(midiccionario)
print(midiccionario["clave3"]["dentro"])
print(midiccionario["clave2"].upper())
print( sorted( midiccionario["clave3"]["dentro"], reverse=True ) )
print( list( reversed( midiccionario["clave3"]["dentro"] ) ) )
plato={"desayuno":"cafe con leche", "cena":"sopa"}
print(plato)
plato["comida"]="pasta" # Si esa clave ya existe en el diccionario le cambia el valor, sino lo crea
print(plato)

# No se pueden anadir metodos a los diccionarios
