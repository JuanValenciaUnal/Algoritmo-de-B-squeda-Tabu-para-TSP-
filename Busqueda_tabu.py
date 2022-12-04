# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:22:28 2022

@author: Juan
"""

def inicializar(pesos):
    camino=[]
    for i in range(len(pesos[0])):
        camino.append(i+1)
    return camino

def calcular_peso(camino,pesos):
    peso=0
    for i in range(len(camino)-1):        
        peso=peso + pesos[camino[i]-1][camino[i+1]-1]
    peso= peso + pesos[camino[-1]-1][camino[0]-1]
    return peso   

def estabu(lista,lista_tabu):
    band =0
    for i in range(len(lista_tabu)):
        
        if(lista_tabu[i][0] in lista):
            if(lista.index(lista_tabu[i][0]) != len(lista)-1):
                if (lista[lista.index(lista_tabu[i][0])+1] == lista_tabu[i][1]):
                      band =1
    if( band == 1):
        return True
    else:
        return False
                

def vecinos(camino,lista_tabu):
    vecinos = []
    for i in range(len(camino)):
        nuevo=camino.copy()
        nuevo[i-1],nuevo[i] = nuevo[i],nuevo[i-1]
        if(estabu(nuevo,lista_tabu) == False):
            vecinos.append(nuevo)
    return vecinos

def menor_vecino(vecinos,pesos):
    vecino_menor=vecinos[0]
    vecino_menor_p = calcular_peso(vecinos[0], pesos)
    for i in range(len(vecinos)):
        if(vecino_menor_p > calcular_peso(vecinos[i], pesos)):
            vecino_menor = vecinos[i]
            vecino_menor_p= calcular_peso(vecinos[i], pesos)
            
    return vecino_menor,vecino_menor_p

def tabu(distancias,lista_tabu,tenencia_tabu,criterio_aspiracion,camino,peso):    
    vecinos(camino, lista_tabu)
    
        
pesos = [[0,2,3,4,1],[1,0,4,1,2],[2,3,0,2,3],[3,4,1,0,4],[4,1,2,3,0]]
lista_tabu= []
tenencia_tabu=3



camino=inicializar(pesos)
peso_inicial= calcular_peso(camino,pesos) 
tenencia_tabu =3

camino=[1,2,3,4,5]
#print(camino)
#print(calcular_peso(camino, pesos))
#print(vecinos(camino, lista_tabu))
vecino_act=vecinos(camino, lista_tabu)
print(menor_vecino(vecino_act, pesos))
#tabu(pesos, lista_tabu, tenencia_tabu, peso_inicial, camino, peso_inicial)

