from collections import Counter

def f(s):
    p = min([i for i in range(2, int(s**0.5) + 1) if s % i == 0])
    return f(s//p) - s if p in bad_primes else f(s//p) + s

bad_primes = set(map(int, input().split()))
n = int(input())
arr = list(map(int, input().split()))

max_beauty = 0
for _ in range(n):
    for i in range(1 << n):
        subset = [arr[j] for j in range(n) if (i & (1 << j))]
        gcd = Counter(subset).most_common(1)[0][0]
        beauty = f(gcd)
        max_beauty = max(max_beauty, beauty)

print(max_beauty)
