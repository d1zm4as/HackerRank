if __name__ == '__main__':
    
    lista = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lista.append([name,score])
    """
    notas = []

    nomes = []
    for x in lista:
        notas.append(x[1])


    menor = min(notas)

    notas_2 = [x for x in notas if x != menor]

    menor2 = min(notas_2)
    for x in lista:
        if x[1]==menor2:
            nomes.append(x[0])
    for x in (sorted(nomes)):
        print(x)
    """
menor = min([x[1] for x in lista])
menor2 = min([x[1] for x in lista if x[1] != menor])
nomes = sorted([x[0] for x in lista if  x[1]==menor2])
for x in nomes:
    print(x)
