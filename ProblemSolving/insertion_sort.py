n = int(input().strip())

array = list(map(int, input().rstrip().split()))

for i in range(1, len(array)):
        key_item = array[i]
        
        j = i - 1       

        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
            lista = [str(x) for x in array]
            print(" ".join(lista))
        array[j + 1] = key_item
lista = [str(x) for x in array]
print(" ".join(lista))
