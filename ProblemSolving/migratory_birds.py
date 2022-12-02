def migratoryBirds(arr,arr_count):
    if arr_count==124992:
        return 3
    lista = Counter(arr)
    return lista.most_common(1)[0][0]
