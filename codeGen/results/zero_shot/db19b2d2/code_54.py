import sys

n, m, h = map(int, input().split())
s = list(map(int, input().split()))

players_in_h = sum(s[i-1] for i in range(1, m+1) if i == h)

probability = (sum(s) - players_in_h) ** n / (m**n)

if sum(s) < n:
    print(-1)
else:
    print(probability)
