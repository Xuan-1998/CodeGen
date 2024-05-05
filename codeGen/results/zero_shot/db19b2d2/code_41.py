n, m, h = map(int, input().split())
s = list(map(int, input().split()))
t = sum(s)
k = s[h-1]

if t < n:
    print(-1)
else:
    print(1 - (t-k) / t)
