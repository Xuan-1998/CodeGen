import sys

def good_subsequences(n, a):
    # Step 1: Calculate the number of ways to choose each element
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        if a[i - 1] % i == 0:
            dp[i] += dp[i - 1]
    
    # Step 2: Calculate the total number of good subsequences
    total_good_subsequences = sum([pow(10, 9, 10**9 + 7) * dp[i] for i in range(n + 1)])
    
    return total_good_subsequences % (10**9 + 7)

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
print(good_subsequences(n, a))
