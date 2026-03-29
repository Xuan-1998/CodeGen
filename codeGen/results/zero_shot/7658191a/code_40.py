def max_score(n, k, z):
    scores = [0] * (n + 1)
    for i in range(1, n + 1):
        scores[i] = arr[i - 1]
    
    max_score = 0
    for i in range(1, n - k + 1):
        for j in range(i, min(i + z + 1, n)):
            score = scores[j]
            if j > i:
                score += scores[j - 1]
            else:
                score += arr[i - 1]
            max_score = max(max_score, score)
    
    return max_score

t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    arr = list(map(int, input().split()))
    print(max_score(n, k, z))
