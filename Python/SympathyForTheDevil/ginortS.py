a = input()
low = [x for x in a if x.islower()==True]
tall = [x for x in a if x.isupper()==True]
num = [ x for x in a if x in "0987654321"]
impar = [x for x in num if int(x) %2!=0 ]
par = [x for x in num if int(x) %2==0 ]

low.sort()
tall.sort()
impar.sort()
par.sort()
for x in tall:
    low.append(x)
for x in impar:
    low.append(x)
for x in par:
    low.append(x)

print("".join(low))
