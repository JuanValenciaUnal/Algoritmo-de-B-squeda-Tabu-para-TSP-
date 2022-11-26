# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 16:20:46 2022

@author: Juan
"""

from sys import maxsize
from itertools import permutations
ciudades = 4

def  tsp(grafo, tamano):
    vertices= []
    for i in range(ciudades):
        if i != tamano:
            vertices.append(i)
            
    min_path = maxsize
    siguiente_permutacion = permutations(vertices) 
    for i in siguiente_permutacion:
        actual_peso =0
        k= tamano
        for j in i:
            actual_peso += grafo[k][tamano]
            k= j
        actual_peso += grafo[k][tamano]
        min_path= min(min_path, actual_peso)
        
    return min_path