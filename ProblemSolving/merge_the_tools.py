def merge_the_tools(string, k):
    occur = set()
    for i in range(len(string)):
        occur.add(string[i])
        if (i+1) % k == 0:
            print(''.join(occur))
            occur = set()
