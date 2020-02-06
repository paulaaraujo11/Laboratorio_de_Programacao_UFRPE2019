"""Universidade Federal Rural de Pernambuco
BSI - 2019.2 Laboratório de Programação
Autora: Paula Araujo"""

#N - N° de regioes, A - regiao origem, B - regiao final
N, A, B = [int(i) for i in input().split()]
#A e B são subtraidos uma unidade para serem manipulados dentro da lista, já q a contagem de lista iniciamem zero
#o mesmo ocorre para P e Q
A -=1
B -=1

grafo=[[] for i in range(N)]#o grafo será uma lista de adjacencia

for j in range(N-1):
    #P- cidade, Q- vizinho, D- distancia entre Q e D    
    P, Q, D = [int(j) for j in input().split()]
    P -=1
    Q -=1
    grafo[P].append((Q,D))#adiciona indo
    grafo[Q].append((P,D))#adiciona voltando


L = [(A,0)]#fila q armazena tuplas c/ regiao e distancia dela com a origem
distancia = [float('inf') for i in range(N)]#armazena as distancias,todas começam com infinito
distancia[A] = 0#distancia da origem para a origem é sempre zero

while L != []:#deve acabar quando a fila acabar
    vertice_atual, custo= L.pop() #cria duas variaveis e add em L
    for VIZINHO in grafo[vertice_atual]:
        if  distancia[VIZINHO[0]] > VIZINHO[1] + custo:#Se a distancia armazenada na lista "distancia" for maior que a distancia armazenada no grafo + o custo da anterior
            distancia[VIZINHO[0]] = VIZINHO[1] + custo #ela recebe o valor da distancia do grafo+o custo anterior
            L.append(( VIZINHO[0],distancia[VIZINHO[0]] ))#mudo os valores na fila L

print(distancia[B])#mostro o menor