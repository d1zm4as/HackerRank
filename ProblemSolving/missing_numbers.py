def missingNumbers(arr, brr):
    # Write your code here
    a = Counter(arr)
    
    b = Counter(brr)
    
    c = b-a
    return sorted(c.keys())
