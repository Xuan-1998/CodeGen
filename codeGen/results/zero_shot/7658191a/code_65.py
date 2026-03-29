def max_score(n, k, z, scores):
    max_score = sum(scores)
    left_moves = min(k, z)

    for i in range(1, n):
        if left_moves > 0 and i - left_moves >= 1:
            new_score = scores[i-1] + max_score
            max_score = max(max_score, new_score)
            left_moves -= 1
        else:
            max_score += scores[i]

    return max_score

t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    scores = list(map(int, input().split()))
    print(max_score(n, k, z, scores))
