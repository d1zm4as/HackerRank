def breakingRecords(scores):
    
    menor = maior =scores[0]
    maiores = menores =0
    for x in scores:
        if x > (maior):
            maior = x
            maiores+=1
        elif x< (menor):
            menor = x
            menores+=1
    return maiores,menores
