def buscador_de_navios(malha,navios, i, j, pos):
  if malha[i-1][j] == '#':
    navios[pos].append((i-1, j))
    malha[i-1][j] = '.'
    buscador_de_navios(malha, navios, i-1, j, pos) 
  if malha[i][j-1] == '#':
    navios[pos].append((i, j-1))
    malha[i][j-1] = '.'
    buscador_de_navios(malha, navios, i, j-1, pos)
  if malha[i+1][j] == '#':
    navios[pos].append((i+1, j))
    malha[i+1][j] = '.'
    buscador_de_navios(malha, navios, i+1, j, pos)
  if malha[i][j+1] == '#':
    navios[pos].append((i, j+1))
    malha[i][j+1] = '.'
    buscador_de_navios(malha, navios, i,j+1, pos) 


pos = 0
navios_atingidos = 0

N, M = list(map(int, input().split()))

malha = []
malha.append(['.' for i in range(M+2)])

#x é uma variavel temporaria para separar strings
for i in range(1, N+1):
  x = ' '.join(input()).split()
  malha.append(['.']+ x +['.'])
malha.append(['.' for i in range(M+2)])

m = len(malha)
navios = []

for i in range(1, m):
  for j in range(1, M+1):
    if malha[i][j] == '#':
      malha[i][j] = '.'
      navios.append([(i, j)])
      buscador_de_navios(malha, navios, i, j, pos) 
      pos+=1
  
disparos_adv = []
n_disparos = int(input())

for j in range(n_disparos):
  L, C = list(map(int, input().split()))
  disparos_adv.append((L, C))

for i in range(len(disparos_adv)):
  for j in range(len(navios)):
    if disparos_adv[i] in navios[j]:
      navios[j].pop(disparos_adv[i])

for i in navios:
  if i == []:
    navios_atingidos += 1
print(navios_atingidos)