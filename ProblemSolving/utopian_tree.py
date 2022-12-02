def utopianTree(n):
    cont =0
    altura =1
    for x in range(0,n):
        cont+=1
        if cont%2==0:
            altura+=1
        if cont%2!=0:
            altura*=2
    return altura
