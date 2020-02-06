def busca_no_campo(linha, coluna, campo):
    if campo[linha][coluna] == "#":
        return
    if campo[linha][coluna] == "k":
        global oPasto
        oPasto += 1
    if campo[linha][coluna] == "v":
        global lPasto
        lPasto += 1
    if campo[linha][coluna] != "#":
      campo[linha][coluna] = "#"

    busca_no_campo(linha-1,coluna,campo)
    busca_no_campo(linha+1,coluna,campo)
    busca_no_campo(linha,coluna-1,campo)
    busca_no_campo(linha,coluna+1,campo)

linha,coluna = [int(x) for x in input().split(" ")]

campo = []
for x in range(linha+2):
    campo.append(["#"] * (coluna+2))

L = []
for x in range(linha):
  pastejo = input()
  L.append(pastejo)

for i in range(1,linha+1):
    for j in range(1,coluna+1):
        campo[i][j] = L[i - 1][j - 1]

ovelha = lobo = 0   
for i in range(1,linha+1):
    for j in range(1,coluna+1):
      oPasto = lPasto = 0
      busca_no_campo(i,j,campo)
      if oPasto > lPasto:
        ovelha += oPasto
        lPasto = 0
      else:
        lobo += lPasto
        oPasto = 0

print(ovelha , lobo)