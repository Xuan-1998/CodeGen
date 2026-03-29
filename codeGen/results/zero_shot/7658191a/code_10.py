def max_score(n, k, z, a):
    score = 0
    moves_to_left = 0

    for i in range(k):
        if moves_to_left > z or (i < k - 1 and a[i + 1] > a[i]):
            # Move right to increase score
            score += a[i]
        else:
            # Move left to decrease score
            score -= a[i]
            moves_to_left += 1

    return score

t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    a = list(map(int, input().split()))
    print(max_score(n, k, z, a))
