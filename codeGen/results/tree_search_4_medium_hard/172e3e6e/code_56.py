def count_good_subsequences(n, a):
    MOD = 10**9 + 7

    # Initialize memoization dictionary
    dp = {(i, []): 1 for i in range(1, n+1)}

    for i in range(1, n+1):
        for j in range(i):
            if a[i-1] % (j+1) == 0:
                if (j, []) not in dp:
                    dp[(i, [j+1])] = 0
                dp[(i, [j+1])] += dp.get((j, []), 0)
        for divisors in list(dp.values()):
            new_divisors = set(divisors) | {a[i-1]}
            if (i, tuple(sorted(new_divisors))) not in dp:
                dp[(i, tuple(sorted(new_divisors)))] = 0
            dp[(i, tuple(sorted(new_divisors)))] += dp.get((i-1, tuple(sorted(divisors))), 0)

    # Return the total count of good subsequences modulo 10^9 + 7
    return sum(dp.values()) % MOD

# Example usage:
n = int(input())
a = list(map(int, input().split()))
print(count_good_subsequences(n, a))
