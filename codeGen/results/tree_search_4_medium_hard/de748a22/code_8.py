import sys

def update_dp(i, j):
    # Calculate sign-variable sum of elements in range [i-j+1, i-1]
    sign_var_sum = 0
    for k in range(j-1, -1, -1):
        if arr[k] == '+':
            sign_var_sum += 1
        else:
            sign_var_sum -= 1
    
    # If sign-variable sum is non-zero, remove at least one element to make it zero
    if sign_var_sum != 0:
        return j+1
    
    # Check if sign-variable sum changes sign within consecutive elements
    for k in range(j-2, -1, -1):
        if arr[k] == '+' and arr[k+1] == '-':
            return j-k
        elif arr[k] == '-' and arr[k+1] == '+':
            return j-k
    
    # If sign-variable sum remains the same or doesn't change sign, remove one element from a pair
    for k in range(j-2, -1, -1):
        if arr[k] != arr[k+1]:
            return 2
    
    return 0

n, q = map(int, input().split())
arr = list(input())
dp = [[0]*(n+q) for _ in range(n+q)]

for i in range(1, n+q):
    dp[i][i-1] = i
for i in range(1, n+q):
    for j in range(i-1, -1, -1):
        dp[i][j] = update_dp(i, j)

for _ in range(q):
    l, r = map(int, input().split())
    print(min(dp[r][l], dp[l-1][r-1]))
