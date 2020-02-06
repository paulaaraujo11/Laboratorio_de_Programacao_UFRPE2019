N = int(input("Quantos são os retângulos?"))
 
cuts = (list(map(int,input("Agora digite as alturas em sequencia: ").split(" "))))

if (len(cuts)) != N:
  print("Quantidade de retângulos inválido, reinice o programa.")
else:
  local_cut = 2
  global_cut = 2

  paper_plates = []

  for i in range(len(cuts)):
    paper_plates.append((cuts[i], i+1))

  paper_plates_ord = sorted(paper_plates)

  scissors = [1 for i in range(len(cuts)+2)]
  scissors[0] = 0
  scissors[len(cuts)+1] = 0

  last = -1

  for i in paper_plates_ord:
    h, index =  i
    scissors[index] = 0
    if last != h:
      if local_cut > global_cut:
        local_cut = global_cut
      last = h
    if scissors[index-1] and scissors[index+1]:
      global_cut+=1

  print("O total de pedaços máximos é %d" %global_cut)