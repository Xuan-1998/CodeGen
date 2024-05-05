from math import comb

n = int(input())
m = list(map(int, input().split()))
ans = 1
for i in set(m):
    ans *= comb(n-1, m.count(i)-1)
print(ans % (10**9 + 7))
