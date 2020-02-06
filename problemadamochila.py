import numpy as np

def mochila(c, peso, valor, n):
    K = [[0 for x in range(c+1)] for x in range(n+1)]
 
    for i in range(n+1):
        for w in range(c+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif peso[i-1] <= w:
                K[i][w] = max(valor[i-1] + K[i-1][w-peso[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    i = n
    j = c
    k = 0
    prod=[]
    index=[]
    while K[i][j] >0:
        if K[i-1][j] != K[i][j]:
            prod.append(peso[valor.index(valor[i-1])])
            index.append(valor.index(valor[i-1])+1)
            j = j - peso[i-1] 
        i = i-1
        
    index.sort()        
    prod.sort()
    
    return index, prod, K[n][c]

n,c = [int(i) for i in input().split()]
peso, valor  = [int(i) for i in input().split()]
#valor = [int(i) for i in input().split()]

index, prod, valor = mochila(c, peso, valor, n)
print(valor)