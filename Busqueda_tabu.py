# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:22:28 2022

@author: Juan
"""

def incializar(pesos):
    camino=[]
    for i in range(len(pesos[0])):
        camino.append(i+1)
    return camino

def calcular_peso(camino,pesos):
    peso=0
    for i in range(len(camino)-1):        
        peso=peso + pesos[camino[i]-1][camino[i+1]-1]
        print(peso," ",camino[i]-1," ",camino[i] )
    peso= peso + pesos[camino[-1]-1][camino[0]-1]
    return peso    

def vecinos(camino,lista_tabu):
    vecinos = []
    for i in range(len(camino)):
        nuevo=camino.copy()
        nuevo[i-1],nuevo[i] = nuevo[i],nuevo[i-1]
        vecinos.append(nuevo)
    return vecinos        
        
pesos = [[0,2,3,4,1],[1,0,4,1,2],[2,3,0,2,3],[3,4,1,0,4],[4,1,2,3,0]]
lista_tabu= []
tenencia_tabu=3
criterio_aspiracion = 100000


#camino=incializar(pesos)
camino=[1,2,3,4,5]
#print(camino)
#print(calcular_peso(camino, pesos))
print(vecinos(camino, lista_tabu))


