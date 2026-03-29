def count_good_subsequences(a):
    n = len(a)
    dp = { (0, i): 1 for i in range(1, n+1) }
    
    for i in range(1, n):
        if a[i] % i == 0:  # Check if a[i] is divisible by i
            for pre in range(i, n):
                dp[(i, pre)] = (dp.get((pre, i), 0) + 1) % (10**9 + 7)
    
    return sum(dp.values()) % (10**9 + 7)

# Example usage:
n = int(input())
a = list(map(int, input().split()))
print(count_good_subsequences(a))
