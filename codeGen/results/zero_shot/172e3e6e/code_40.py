def count_good_subsequences(a):
    MOD = 10**9 + 7
    n = len(a)

    # Base case: no good subsequences with length 0
    f = [0] * (n+1)
    f[0] = 1

    for k in range(1, n+1):
        for i in range(2, k+1):
            if a[k-1] % i == 0:
                f[k] += f[i-1]
                f[k] %= MOD
        f[k] += f[k-1]
        f[k] %= MOD

    return f[n]

# Example usage:
n = int(input())
a = [int(x) for x in input().split()]
print(count_good_subsequences(a))
