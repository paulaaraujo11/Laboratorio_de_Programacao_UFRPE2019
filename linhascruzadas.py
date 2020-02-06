N = input()
cruzamentos = 0
x = 1 #x é uma variável qualquer temporária
pregos = [int(i) for i in input().split()]
for i in range(len(pregos)-1,0,-1):
    for j in range(len(pregos)-1-x,-1,-1):
        if pregos[j] > pregos[i]:
          cruzamentos +=1
    x += 1
print(cruzamentos)