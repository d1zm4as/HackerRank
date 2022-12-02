def diagonalDifference(arr):
    l_d = d_l = 0
    for i in range(n):
        l_d += arr[i][i]
        d_l += arr[i][n-1-i]
    return abs(l_d-d_l)
