def findDigits(n):
    lista = [int(x) for x in str(n)]
    cont = 0
    for x in lista:
        if x==0:
            pass
        elif n%x==0:
            cont+=1
    return cont
