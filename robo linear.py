#Universidade Federal Rural de Pernambuco - Dept. de Estatística e Informática
#BSI - 2019.2 - Laboratório de Informática
#Autora: Paula Priscila da C. Araujo

#Programa feito para calcular o número de metros deslocados de um robo 'o RL2' através de 2 comandos.
print('='*20,' CONTADOR DE DESLOCAMENTO DO RL2', '='*20)
print('Use os comandos F p/frente e T p/trás,qualquer outro será desconsiderado! \n')
while True:
    #usuario insere uma cadeia de strings com comandos,que é jogado para letras maiusculas
    comandos = str(input('Digite os comandos desejados [SAIR p/parar]: ')).upper()
    if comandos == 'SAIR':
        break
    #conta quantas vezes cada letra foi vista na cadeia
    passos_f = comandos.count('F')
    passos_t = comandos.count('T')

    #o programa calcula quantos passos serão dados de acordo com a qntd de letras 'F' e 'T' na cadeia
    if passos_f > passos_t:
       total = passos_f - passos_t
       print(f'O RL2 deslocará {total}m para frente\n')
    elif passos_f == passos_t:
        print('O deslocamento do RL2 é 0\n')
    else:
        total = passos_t - passos_f
        print(f'O RL2 deslocará {total}m para trás\n')
        
    

