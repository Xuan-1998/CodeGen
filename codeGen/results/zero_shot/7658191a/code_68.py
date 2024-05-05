def max_score(n, k, z, a):
    score = 0
    for i in range(1, n + 1):
        if i <= k and i <= z:
            # Make left moves until we reach the limit or the end of the array
            while i <= k and i <= z:
                score += a[i - 1]
                i -= 1
                if i > 0:
                    k -= 1
                    z = min(z, k)
        else:
            # Make right moves until we reach the end of the array or the limit
            while i < n and k > 0:
                score += a[i]
                i += 1
                k -= 1
    return score

t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    a = list(map(int, input().split()))
    print(max_score(n, k, z, a))
