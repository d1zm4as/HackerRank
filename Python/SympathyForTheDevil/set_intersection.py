N1 = int(input())
storage1 = set(input().split());

N2 = int(input())
storage2 = set(input().split());

storage3 = storage1.intersection(storage2)

print(len(storage3))