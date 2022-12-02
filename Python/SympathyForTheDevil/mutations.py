def mutate_string(s, p, c):
    lista = [x for x in s]
    lista[p] = c
    
    return "".join(lista)
