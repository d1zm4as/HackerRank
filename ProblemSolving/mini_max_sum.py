def miniMaxSum(arr):
    max_value = sum(arr)-min(arr)
    min_value= sum(arr) - max(arr)
    print(f'{min_value} {max_value}')
