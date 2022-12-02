cube = lambda x: x**3 

def fibonacci(n):
    lis = [0,1]
    for x in range(2,n):
        lis.append(lis[x-2]+lis[x-1])
    return (lis[0:n])
