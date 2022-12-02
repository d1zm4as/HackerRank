a = int(input())
for x in range(a):
    A = int(input())
    lol = {x for x in input().split()}
    B = int(input())
    ex = {x for x in input().split()}
    if lol<=ex:
        print(True)
    else:
        print(False)
