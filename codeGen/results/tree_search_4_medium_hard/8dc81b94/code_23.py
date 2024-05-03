def can_make_zero(arr):
    n = len(arr)
    
    memo = {}
    
    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == 0 and j == n - 1: 
            return arr[0] == 0
        elif i == 0: 
            return arr[j] <= 0 or dp(0, j-1)
        elif j == n - 1:
            return arr[i] >= 0 or dp(i+1, n-1)
        
        if abs(arr[i]) > abs(arr[j]):
            return arr[i] <= 0 or dp(i+1, j) or dp(i, j-1)
        else:
            return arr[j] <= 0 or dp(i, j-1)
        
        memo[(i, j)] = res
        return res
    
    return "YES" if dp(0, n-1) else "NO"


# Read input from stdin
while True:
    try:
        n = int(input())
        arr = list(map(int, input().split()))
        print(can_make_zero(arr))
    except EOFError:
        break
