def max_score(n, k, z, arr):
    max_score = 0
    for i in range(1, n + 1):
        score = 0
        for j in range(i):
            if k > 0:
                if z > 0 and i - j > 2:
                    k -= 1
                    score += arr[i - 1]
                else:
                    k -= 1
                    score += arr[j + 1]
            if score > max_score:
                max_score = score
    return max_score

t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    arr = list(map(int, input().split()))
    print(max_score(n, k, z, arr))
