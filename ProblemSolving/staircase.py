def staircase(n):
    a = '#'
    for x in range(1,n+1):
        b = a*x
        print(b.rjust(n))
