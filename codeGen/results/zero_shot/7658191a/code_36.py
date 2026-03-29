def max_score(scores, k, z):
    score = 0
    left_moves = min(k, z)
    for i in range(1, len(scores)):
        if i <= left_moves:
            score += scores[i - 1]
        else:
            score += scores[i]
        k -= 1
        if k == 0:
            break
    return score

t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    scores = list(map(int, input().split()))
    print(max_score(scores, k, z))
