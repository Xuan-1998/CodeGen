def solve(n, a):
    MOD = 10**9 + 7
    count = 0
    for i in range(n):
        count += count_good_subsequences(a[:i+1], i)
    return count % MOD

n = int(input())
a = [int(x) for x in input().split()]
print(solve(n, a))
