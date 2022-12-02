ef twoArrays(k, A, B):
    
    A.sort(reverse=True)
    B.sort()
    for x in range(0,len(B)):
        if (A[x])+(B[x])<k:
            return "NO"
    return "YES"
