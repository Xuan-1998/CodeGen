r = {}
for _ in range(N):
    u = int(input())
    r[u] = r.get(u, 0) + 1

for _ in range(M):
    l = int(input())
    r[l] = r.get(l, 0) + 1

T = int(input())
for _ in range(T):
    N, M, C = map(int, input().split())
    results = []
    for c in range(1, C+1):
        count = 0
        for u in sorted(r.keys()):
            if u <= c:
                count += r[u]
            else:
                break
        for l in sorted(r.keys(), reverse=True):
            if l <= c:
                count += r[l]
            else:
                break
        results.append(count % (10**9+7))
    print(*results, sep=' ')
