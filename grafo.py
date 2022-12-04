import networkx as nx
import matplotlib.pyplot as plt
from Nodos import *



def agregar_arista(G, u, v, dist, di=False):
    G.add_edge(u, v, weight=dist)
    
#dis = [[0,2,3,4,1],[1,0,4,1,2],[2,3,0,2,3],[3,4,1,0,4],[4,1,2,3,0]]
#ciudades= ["A","B","C","D","E"] 
    
if __name__ == '__main__':
    # Instantiate the DiGraph
    G = nx.DiGraph()
    
    #ciudades= ["a","b","c","d","e"]   


    #dis = [[0,2,3,4,1],[1,0,4,1,2],[2,3,0,2,3],[3,4,1,0,4],[4,1,2,3,0]]
    
    
    
    for i in range(len(ciudades)):
        
        for j in range(len(ciudades)):
            
            if distancias[i][j] != 0:
                
                agregar_arista(G, ciudades[i], ciudades[j],distancias[i][j])
            
            

    #dibujar el grafo
    pos = nx.layout.random_layout(G)
    nx.draw_networkx(G, pos)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Recorrido del vendedor")
    plt.show()    
      

    
        
       
        
        
        