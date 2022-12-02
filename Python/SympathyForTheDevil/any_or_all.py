#  return any([x for x in range(0,1000) if x == 45]) -> retorna True se ALGUM elemento == 45
#  return all([x for x in range(0,1000) if x ==45])-> retorna True se TODOS os items forem == 45


a, b = int(input()),input().split()
print(all([int(x) > 0 for x in b])==True and any(x==x[::-1] for x in b))
