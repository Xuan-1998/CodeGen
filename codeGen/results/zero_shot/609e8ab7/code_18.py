n = int(input())
p = list(map(int, input().split()))
l = []
r = []

for _ in range(n):
    l_i, r_i = map(int, input().split())
    l.append(l_i)
    r.append(r_i)

values = {i+1: (l_i, r_i) for i, (l_i, r_i) in enumerate(zip(l, r))}

def dfs(vertex):
    if not values[vertex]:
        return 0

    l_i, r_i = values[vertex]
    diff = min(abs(l_i - l), abs(r_i - r)) for l, r in zip(l, r) if l <= l_i <= r or l <= r_i <= r]

    res = dfs(p[vertex])
    res += (r_i - l_i) // diff + ((r_i - l_i) % diff != 0)

    return res

res = 0
for i in range(1, n+1):
    res += dfs(i)
print(res)
