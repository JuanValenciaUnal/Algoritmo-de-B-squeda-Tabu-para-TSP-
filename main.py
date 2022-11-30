import networkx as nx
import matplotlib.pyplot as plt


def agregar_arista(G, u, v, dist, di=False):
    G.add_edge(u, v, weight=dist)
    
if __name__ == '__main__':
    # Instantiate the DiGraph
    G = nx.DiGraph()
    
    ciudades= ["a","b","c","d","e"]   


    dis = [[0,2,3,4,1],[1,0,4,1,2],[2,3,0,2,3],[3,4,1,0,4],[4,1,2,3,0]]
    
    for i in range(len(ciudades)):
        
        for j in range(len(ciudades)):
        
            dist=dis[i][j]
          
            agregar_arista(G, i, j,dist)
            
            

    #dibujar el grafo
    pos = nx.layout.random_layout(G)
    nx.draw_networkx(G, pos)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Recorrido del vendedor")
    plt.show()    
      

    
        
       
        
        
        