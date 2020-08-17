#!/usr/bin/env python
'''
Funciones de uso específico
------------------------------------
Autor: Alejandro Rodriguez Salas

Descrpción:
Programa creado para resolver ejercicios
propuestos del Módulo 4 del curso 
de Python inicial
'''

__author__ = "Alumno: Alejandro Rodriguez Salas"
__email__ = "ale_rodra@live.com.ar"

import random

def promedio(numeros):
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