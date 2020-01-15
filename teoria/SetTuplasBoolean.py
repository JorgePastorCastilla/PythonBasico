# BOOLEANS #
True
False
1
0
print(2>1)
# TUPLAS #
# Tuplas son secuencias inmutables
# Las tuplas se definen con ()
mitupla=(1,2,3)
print(mitupla[0])
tupla=("paquito",1,True) # Permiten varios tipos de valores
print(tupla)
print(tupla+mitupla) # Las tuplas pueden sumarse
# SET #
# Los set son conjuntos desordenados de elementos unicos
# Los set se definen con {}
miset={1,1,1,1,1,1,1,2,2,2,2,3,3,3,3,3,3}
print(miset)
s={1,2,3}
s.add(4)
print(s)

# Convertir una lista en un set
conversion=set([1,1,1,1,1,1,2,2,2,2,3,3,3,3,3,3])
print(conversion)