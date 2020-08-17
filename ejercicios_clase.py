#!/usr/bin/env python
'''
Funciones [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"

import random


def imprimir_nombre(nombre, apellido):
    '''
    En este lugar debe colocar el "print" e imprimir en \n
    pantalla el nombre y apellido que vienen por parámetro'''
    print(nombre,apellido)


def promedio(numeros):
    
    # Alumno:
    # 1) calcule el promedio
    # 2) use "return" para retornar ese valor
     # Cuando termine de implementar está función borrar "pass"
     '''
     Devuelve el promedio obtenido de la lista de \n
     (numeros) tomados como parametros
     '''
     prom = sum(numeros) / len(numeros)
     return prom


def ordenar (numeros):
    '''
    Devuelve la lista de (numeros) ingresados por \n
    parametros de forma ordenada de mayor a menor
    '''
    numeros.sort(reverse=True)
    return numeros


def lista_aleatoria(inicio,fin,cantidad):
    '''
    Genera lista de numeros ramdon de cuyas\n
    características son ingresadas por paramatro\n
    números entre (inicio,fin) cantidad de números(cantidad)
    '''
    lista = []
    lista.clear()
    for i in range(cantidad):
        numero = random.randrange(inicio, fin+1)
        lista.append(numero)
    
    return lista
        
    
def contar(lista_numeros,numero):
    '''
    contar la cantidad de veces que aparece un\n
    número especificado dentro de la lista
    Ambas ingresadas por parametro(lista_numeros,numero)
    '''
    cont = lista_numeros.count(numero)
    return cont


def ej1():
    print('Mi primera funcion')
    # Realice una función llamada "imprimir_nombre"
    # la cual reciba dos parámetros, el nombre y el apellido
    # Esa función ya se encuentra a medio armar al principio de este archivo.
    # Debe cumpletar la función para que se imprima en pantalla su nombre y apellido
    # Debe invocar a la función como:
    imprimir_nombre('Alejandro', 'Rodriguez Salas')

    # Reemplazar por su nombre y apellido los textos


def ej2():
    # Ejercicios con funciones del sistema
    numeros = [2, 4, 6, 8, 10, 12]
    
    '''
    Realice una funcion llamada "promedio" la cual
    reciba como parámetro una lista de números y calcule
    el promedio de ella como:
    promedio = sumatoria_numeros / cantidad_numeros

    Resuelva la sumatoria y la cantidad con las herramientas
    que desee, recomendamos usar las funciones disponibles
    de Python para ello o en tal caso realizar un bucle.
    Puede utilizar la función "sum" y la función "len"
    sum --> obtener la sumatoria de números
    len --> obtener la cantidad de números
    promedio = sumatoria_numeros / cantidad_numeros

    La función debe retornar (return) el promedio calculado
    La función debe contemplar si se le pasa una lista vacia
    (es decir, de "0" elementos)

    Utilice esa función para calcular el promedio y luego
    imprima en pantalla el resultado

    '''
    # La función ya se encuentra definida arriba de todo en el archivo,
    # busque al princpio de todo "def promedio"
    # Ya la función fue preparada para que usted le pase "numeros"
    # como parámetro, falta que calcule el promedio y retorne el valor
    # resultante.

    # Llamar a la función en este lugar y capturar el valor del retorno
    promedio_re = promedio(numeros)

    # Luego imprimir en pantalla el valor resultante, tal que:
    print('El promedio de {} es igual a : {}'.format(numeros,promedio_re))


def ej3():
    # Ejercicios de listas y métodos
    numeros = [2, 4, 6, 8, 10, 12]

    '''
    Generar una una nueva funcion que se llame "ordenar",
    que utilizaremos para odernar la lista de numeros.
    Dentro de la función puede ordenar la lista
    usando bucles o las funciones nativas de Python (sort)

    Aproveche el ejemplo de "promedio" para crear una función
    similar, la debe crear y escribir abajo de ella.

    '''
    
    print(numeros)

    # Luego de crear la función invocarla en este lugar:
    
    lista_ordenada = ordenar(numeros)
    # Imprimir en pantalla "lista_ordenada" que tendrá
    # los valores retornado por la función ordenar
    print('La lista ordena de mayor a menor es:\n',lista_ordenada)


def ej4():
    # Ejercicios con modulos del sistema
    inicio = 0
    fin = 10
    cantidad = 5

    # Ejemplo de como obtener un numero aleatorio
    # entre inicio y fin
    # inicio <= numero <= fin
    numero = random.randrange(inicio, fin+1)
    # Documentación oficial de random
    # https://docs.python.org/3.7/library/random.html
    # Ante cualquier duda preguntar en el campus!

    '''
    Realice una funcion llamada "lista_aleatoria" la cual
    reciba como parámetro el rango de aceptación de la lista
    "inicio y fin" y la cantidad de elementos que deseamos que
    contenga la lista, es decir, la cantidad de elementos random a generar.

    --> def lista_aleatoria (inicio, fin, cantidad)

    Para ello dentro de la función deberá realizar un bucle que repita "cantidad"
    veces esta operacion:
    numero = random.randrange(inicio, fin+1)

    Cada valor generado lo debe guardar en una lista, recuerde:
    1) Iniciar y crear esa lista vacia.
    2) Para agregar nuevos elementos en la lista utiliza "append"

    Finalmente dicha función debe retornar la lista de elementos random generados.
    '''
    

    # Invocar lista_aleatoria
    # mi_lista_aleatorio = lista_aleatoria(inicio, fin, cantidad)
    # print(mi_lista_aleatorio)
    mi_lista_aleatorio = lista_aleatoria(inicio, fin, cantidad)
    print(mi_lista_aleatorio)


def ej5():
    # Ejercicios de listas y métodos
    cantidad_numeros = 5

    '''
    Utilice la función "lista_aleatoria" para generar
    una lista de 5 números en un rango de 1 a 9 inclusive

    Generar una una nueva funcion que se llame "contar",
    que cuenta la cantidad de veces que un elemento pasado
    por parámetro se repite en la lista.
    Para saber cuantas veces se repiten el elemento pasado
    en la lista pueden usar bucles o el método nativo de list
    "count"

    '''

    # Por ejemplo creo una lista de 5 elemtnos
    # lista_numeros = lista_aleatoria(...,...,cantidad_numeros)
    # Luego quiero averiguar cuantas veces se repite el numero 3
    # cantidad_tres = contar(lista_numeros, 3)

    mi_lista_aleatorio = lista_aleatoria(inicio=0,fin=9,cantidad=5)
    numero_tres = contar(mi_lista_aleatorio,numero=3)

    print('La lista de números es:\n',mi_lista_aleatorio)
    print('El número 3 aparece {} veces'.format(numero_tres))



if __name__ == '__main__':
    print('\n                 Bienvenidos a otra clase de Inove con Python      \n')
    print('\n       Ej1:Impresión a travez de una función\n')
    ej1()
    print('\n        Ej2:Función promedio\n')
    ej2()
    print('\n       Ej3:Ordenar lista de números\n')
    ej3()
    print('\n       Ej4:Originar lista con números random\n')
    ej4()
    print('\n       Ej5:Originar lista y contar los números 3\n')
    ej5()

    print('\n******************* FIN DEL PROGRAMA *******************')
