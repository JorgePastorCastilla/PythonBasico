# CONTROL DE FLUJO #
# Operadores logicos
# todo: CONTROL+ALT+L PARA IDENTAR
1 < 2  # menor
2 > 1  # major
1 <= 2  # menor o igual
2 >= 1  # menor o igual
1 == 1  # igual

1 == "1"  # devuelve false
1 == 1  # devuelve true
1 == True  # devuelve true

'hola' != 'adios'  # Distinto (True)

# Operadores logicos

# AND
(1 < 2) and (3 < 4)

# OR
(1 < 2) or (3 < 4)

# operadores logicos multiples
((1 < 2) or (3 < 4)) or (3 > 4)

# if/else
not (1 < 2)  # devuelve false, seria el '!' de java
if (1 < 2):
    print('dentro del primer if')
else:
    print('dentro del else')

# elseif:
if (1 < 2):
    print('dentro del primer if')
elif (3==3):
    print('dentro del else')

# Bucle for
#iterar listas
secuencia = [1,2,3,4,5]
for i in secuencia:
    print(i)
print("\n")
for ii in range(1,6):
    print(ii)

#iterar diccionarios
diccionario = {"key1":1,"key2":2,"key3":3}
for iii in diccionario.values():
    print(iii)
for k,v in diccionario.items():
    print(k)
    print(v)

#iterar tuplas
listatuplas = [(1,2),(3,4),(5,6)]
for item in listatuplas:
    print(item)
for t1,t2 in listatuplas:
    print("key = "+str(t1))
    print("value = "+str(t2))

#iterar string
for c in "hola":
    print(c)
#while
i=1
while (i<5):
    print(i)
    i +=1

# For comprehension
x = [1,2,3,4]
resultado = []
for i in x:
    resultado.append(i+1)
print(resultado)

resultado=[i+1 for i in x]
print(resultado)