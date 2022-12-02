seta = {int(x) for x in input().split()}
b = int(input())
cond = bool
for x in (0,b+1):
    ex = {int(x) for x in input().split()}
    if ex <= seta:
        cond = True
    else:
        cond = False

print(cond)
