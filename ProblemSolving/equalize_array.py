def equalizeArray(arr):
    comum  = mode(arr)
    cont = 0
    for x in arr:
        if x!=comum:
            cont+=1
    return cont
