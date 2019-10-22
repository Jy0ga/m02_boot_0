from functools import reduce

def doble(x):
    return x*x

lista = [1,3,-1,15,9]

listaDobles = map(lambda x: x*2, lista)
listaDobles1 = map(doble, lista)

listaPares= filter(lambda x: x % 2 == 0, lista)

sumatorio = reduce(lambda x,y: x+y, lista)
sumatorioDobles= reduce(lambda x,y: x+y*2, lista)

suma100 = reduce(lambda x,y: x+y, range(101))

print(list(listaDobles))
print(list(listaDobles1))

print(sumatorio)
print(sumatorioDobles)

print(suma100)