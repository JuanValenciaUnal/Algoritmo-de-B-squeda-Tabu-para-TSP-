import random

#ciudades=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"]
ciudades=["A","B","C","D","E"]
distancias=[]

for i in range(len(ciudades)):
    distancias.append
    d_random=[]
    for j in range(len(ciudades)):
        
        if j == i:
            d_random.append(0)
             
        else:
            n_random = random.randint(1,10)
            
            d_random.append(n_random)
            
    distancias.append(d_random)  
    
