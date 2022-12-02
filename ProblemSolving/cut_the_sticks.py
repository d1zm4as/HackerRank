def cutTheSticks(arr):
    lista = sorted([x for x in arr])
    tamanhos = []
    while len(lista)!=0:
        tamanhos.append(len(lista))
        menor = min(lista)
        lista2 = [(x-menor) for x in lista if x != menor]
        lista = [x for x in lista if x!= menor]
    return tamanhos
