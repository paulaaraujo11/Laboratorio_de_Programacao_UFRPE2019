def dijkstra(grafos,O,V):
  initial = O
  end = V-1
  distancia = [float('inf') for i in range(N)]
  distancia[initial] = 0
  L = [(initial,0)]
  while L != []:
    vertice_atual, custo= L.pop() 
    for VIZINHO in grafo[vertice_atual]:
      if  distancia[VIZINHO[0]] > VIZINHO[1] + custo:
        distancia[VIZINHO[0]] = VIZINHO[1] + custo 
        L.append(( VIZINHO[0],distancia[VIZINHO[0]] ))
  return distancia

N, M = [int(i) for i in input().split()]
O  = 0

grafo=[[] for i in range(N)]
 

for j in range(M):
  U, V, W = [int(j) for j in input().split()]
  grafo[U].append((V,W))#adiciona indo
  grafo[V].append((U,W))#adiciona voltando
  dijkstra(grafo,U,W)

#a estrategia seguinte é armazenar as maiores distancias de cada entrada, depois escolher a menor entre elas