#Universidade Federal Rural de Pernambuco - Dept. de Estatística e Informática
#BSI - 2019.2 - Laboratório de Informática
#Autora: Paula Priscila da C. Araujo
#-----------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------
#O algoritmo 'guloso' tentar pintar o grafo com o minimo de cores, ex.: tenta pintar o mapa com 0 cores
#se nao consegue tenta com 1 e assim por diante até pintar todos sem os vizinhos terem a msm cor
#--------------------------------------------------------------------------------------------

#funcao que retorna as cores q irão ter em cada vértice do grafo
def cores_no_grafo(grafo):
    for n_cor_dado in range(1, len(grafo)):
        cores = pinta_grafo(grafo, n_cor)
        if cores:
            return cores
        
#funcao chamada para pintar o grafo        
def pinta_grafo(grafo, n_cor):
    cores = {}
    def vizinhos(nos, cor):
        return all(cor != cores.get(x) for x in nos)
    for no, adj in grafo.items():
        pinta_regiao = False
        for cor in range(n_cor):
            if vizinhos(adj, cor):
                pinta_regiao = 1
                cores[no] = cor
                break
        if not pinta_regiao:
            return None
    return cores
 

print('='*20,'Colorindo Mapas','='*20,'\n')

n_cores=0#as cores iniciam com zero
mapa = {}

n=int(input('Quantas regiões/vértices tem o mapa:'))

for i in range(0,n):#entrada do grafo como dicionario
    chave = input(f"\nChave da {i+1}° região: ").upper()
    vizinhos = input(f"Regiões vizinhas a {chave}: ").upper()
    mapa[chave] = vizinhos

while True:#usa estrutura de repeticao para tentar pintar o mapa
    if pinta_grafo(mapa,n_cores) == None:
        n_cores +=1
    else:
        print('-'*20,'\n')
        print(pinta_grafo(mapa,n_cores))
        print(f'O número de cores necessárias é {n_cores}')
        break
 
