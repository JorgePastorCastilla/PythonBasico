#####################################
######## EXERCICIS DE REPAS  ########
#####################################

################
## Exercici 1 ##
################

# Donat el string:
s = 'django'

# Utilitzar indixos per mostrar els siguents elements de el string:
# 'd'
print(s[0])

# 'o'
print(s[-1])

# 'djan'
print(s[0:4])
print(s[-2])

# 'jan'
print(s[1:4])

# 'go'
print(s[4:6])
print(s[4:])
print(s[-2:])


# Bonus: Utilitza indixos negatius per donar la volta al string
print(s[::-1])
print(''.join(reversed(s)))
################
## Exercici 2 ##
################

# Donada aquesta llista niada:
l = [3,7,[1,4,'hola']]
# Cambia 'hola' por "adeu"
print(l[2][2])
l[2][2] = "adios";
print(l[2][2])
################
## Exercici 3 ##
################

# Utilitzant les claus y els indexos trau el element 'hola' dels seguents diccionaris :

d1 = {'simple_key':'hello'}
print(d1['simple_key'])

d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])

d3 = {'k1':
          [
              {'nest_key':[
                  'this is deep',
                  ['hello']
              ]
              }
          ]
}
print(d3['k1'][0]['nest_key'][1][0])


################
## Exercici 4 ##
################

# Utilitzar set per trobar els elements unics de aquesta llista:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
print(set(mylist))

################
## Exercici 5 ##
################

# Donades dues variables:
age = 4
name = "miperro"

# Utilitzar el metode format per imprimir el seguent string:
"Hola mi perro se llama 'miperro' y tiene 4 anyos"
print("Hola mi perro se llama {} y tiene {} anyos".format(name,age))
print("Hola mi perro se llama {a} y tiene {b} anyos".format(a=name,b=age))
