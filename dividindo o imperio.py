#o imperio

#a entrada ta pronta
N = int(input())

grafo=[[] for i in range(N)]#o grafo será uma lista de adjacencia

for j in range(N-1):
       
    A, B = [int(j) for j in input().split()]
    A -=1
    B -=1
    grafo[A].append(B)#adiciona indo
    grafo[B].append(A)#adiciona voltando

#estrategia : cria uma lista de adjacencia com os vertices ao de maior grau
#varre com busca por ondas seus vizinhos e tentar retirar o vizinho com menor adjacencia
#conta quantas cidades sobraram vizinhas a uma cidade 'x' (por busca tbm) e quantas cidades vizinhas a uma cidade 'y'
#armazena os resultados em uma lista ou matriz
#apresenta na matriz a que teve a menor diferença de cidades!


