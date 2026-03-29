import heapq

def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bad_primes = set(map(int, input().split()))

    # Initialize the dp table with all elements set to -1
    dp = [-1] * (n + 1)
    
    for i in range(1, n + 1):
        # Calculate the GCD of the current number with all other numbers
        gcd = arr[i]
        for j in range(i):
            if gcd < arr[j]:
                gcd = abs((gcd, arr[j]).index(max((gcd, arr[j]))))
        
        # Update the dp table accordingly
        if gcd not in bad_primes:
            dp[i] = max(dp[i], 0) + gcd
        else:
            dp[i] = max(dp[i], 0) - gcd
    
    return sum(dp)

print(solve())
