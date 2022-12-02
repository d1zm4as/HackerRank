def runningTime(array):
    cont = 0
    for i in range(1, len(array)):
        key_item = array[i]
        
        j = i - 1       

        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
            cont+=1
        array[j + 1] = key_item
    return cont
