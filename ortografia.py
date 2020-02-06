def calcular_Distancia(s1, s2):
    m=len(s1)+1
    n=len(s2)+1
    tbl = {}
    for i in range(m): tbl[i,0]=i
    for j in range(n): tbl[0,j]=j
    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if s1[i-1] == s2[j-1] else 1
            tbl[i,j] = min(tbl[i, j-1]+1, tbl[i-1, j]+1, tbl[i-1, j-1]+cost)
    return tbl[i,j]

N, M =  [int(i) for i in input().split()]
p_dicionario = [0 for i in range(N)]
p_analizar = [0 for i in range(M)]

in_dicionario = [[] for i in range(len(p_analizar))]

for i in range(N):
  linha_n = input().lower()
  if (len(linha_n)) > 20:
    break
  p_dicionario[i] = linha_n

for j in range(M):
  linha_m = input().lower()
  if (len(linha_m)) > 20:
    break
  p_analizar[j] = linha_m

print()

for k in p_dicionario:
  for l in p_analizar:
    temp = 0
    if calcular_Distancia(k, l) <= 2:
      in_dicionario[temp][l].append(k)
    temp +=1

for i in in_dicionario:
  if i == []:
    print()
    print()
  else:
    for j in i:
      print(j, end=" ")