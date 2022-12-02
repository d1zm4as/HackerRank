def beautifulDays(i, j, k):
    cont=0
    for x in range(i,j+1):
        normal = "".join([y for y in str(x) ])
        reverso = "".join(reversed([y for y in str(x) ]))
        a = (int(normal)-int(reverso))/k
        if int(a)==a:
            cont+=1
    return cont
