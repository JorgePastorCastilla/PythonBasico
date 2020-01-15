# LISTA
# Son los arrays de Python
# Se define con []

milista = [1,2,3] # Creamos lista
milista2 = ["hola",1,2.3,[0,0,0],'adios']

print(milista)
print(milista2)

#Indexado
print(milista[0])
print(milista[-1])
print(milista[2:])
print(milista[:3])

milista[0] = "prueba"

print(milista[0])

# Metodos de las listas
milista.append("nuevo")
print(milista)

milista3 =  [3,5,6,1,4,2]
print(milista3)
milista3.sort() # ordena
print(milista3)

a = milista3.pop() # elimina
print(a)
print (milista3)

milista.reverse() # gira el orden de la lista
print (milista)

milista4 = [1,2,[3,4]]
print(milista4[2][0])

# Matrices
matriz = [[1,2,3],[4,5,6],[7,8,9]]
print (matriz[1][1])

# Atentos
prim_col = []
for col in matriz:
    prim_col.append(col[0])
print (prim_col)

prim_col2 = [col[0] for col in matriz]
print (prim_col2)
