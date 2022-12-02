def getTotalX(a, b):
    total = 0
    #   Iterate over range between the largest element
    #   in list(a) and the smallest element in list(b)
    for i in range(max(a), min(b) + 1):
        #   Any value != 0 means element 
        #   in 'a' is not a factor of i
        mapA = list(map(lambda x: i % x, a))
        #   Any value != 0 means i is not
        #   a factor of element in 'b'
        mapB = list(map(lambda x: x % i, b))
        #   If all values == 0 then 
        #   solution criteria are met
        if sum(mapA) + sum(mapB) == 0:
            total +=1
    return total
    
