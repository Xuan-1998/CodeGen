def good_subsequences(a):
    MOD = 10**9 + 7
    n = len(a)
    dp = {(1, 0): 1}
    
    for i in range(2, n+1):
        for pre in range(i):
            if a[i-1] % i == 0:
                dp[(i, pre)] = sum(dp.get((j, k), 0) for j in range(1, i)) + (pre == 0)
            else:
                dp[(i, pre)] = 0
    return dp.get((n, n-1), 0) % MOD

# Read input from stdin
n = int(input())
a = [int(x) for x in input().split()]

# Print the result to stdout
print(good_subsequences(a))
