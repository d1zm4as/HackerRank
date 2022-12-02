 """
    lista2 = sum([x for x in bill if x != bill[k]])/2
    return "Bon Appetit" if lista2 == b else int(abs(((sum([x for x in bill if x != bill[k]])/2)-b)))
    """
    lol = bill.pop(k)
    return ("Bon Appetit" if sum(bill)/2 == b else int(b-sum(bill)/2))
