for _ in range(int(input())):
    
    try:
        a,b = [int(x) for x in input().split()]
        print(a//b)
    except ZeroDivisionError as zero:
        print (f"Error Code: {zero}")
    except ValueError as value:
        print(f"Error Code: {value}")
