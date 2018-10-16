__author__='Irvin Mariano'

from MemoriaDinamica import *
lista = []
herramientas = ['carretilla', 'martillo', 'alambre', 'pala', 'taladro']
precios = [350, 100, 80, 75, 230]

listas = MemoriaDinamica(herramientas)
listas.imprimirLista()
listas.ordenarLista()
listas.imprimirLista()
listas.recorrerArreglo()
listas.imprimirLista()
listas.agregarelementoarray('carretilla')
listas.imprimirLista()
listas.eliminarElemento('taladro')
listas.imprimirLista()
lista2 = MemoriaDinamica(precios)
lista2.imprimirLista()
lista2.agregarelementoarray(20)
lista2.imprimirLista()