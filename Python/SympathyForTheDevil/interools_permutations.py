from itertools import permutations

a,b = [x for x in input().split()]
lista = sorted(list(permutations(a, int(b))))
for x in lista:
    print("".join(x))
