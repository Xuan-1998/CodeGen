def count_and(x, k):
    if x == 0:
        return 2**k - (2**(k-1)) if k > 0 else 1
    return 2**k

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    and_count = 0
    for i in range(n):
        x = int(input())
        and_count += count_and(x, k)
    print(and_count % (10**9 + 7))
