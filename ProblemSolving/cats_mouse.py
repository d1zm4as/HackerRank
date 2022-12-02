    
    if abs(x-z) > abs(y-z):
        return "Cat B"
    if abs(y-z) > abs(x-z):
        return "Cat A"
    if abs(x-z) == abs(y-z):
        return "Mouse C"
