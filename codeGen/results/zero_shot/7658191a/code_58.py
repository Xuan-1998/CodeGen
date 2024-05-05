def max_score(n, k, z, arr):
    score = 0
    moves_to_right = 0
    for i in range(1, n+1):
        if moves_to_right >= z or i == n:
            break
        score += arr[i-1]
        moves_to_right += 1
    remaining_moves = k - moves_to_right
    if remaining_moves > 0:
        left_moves = min(z, remaining_moves)
        right_moves = remaining_moves - left_moves
        for _ in range(left_moves):
            score -= arr[i-2]  # move to the left
            i -= 1
        for _ in range(right_moves):
            score += arr[i]  # move to the right
            i += 1
    return score

t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    arr = list(map(int, input().split()))
    print(max_score(n, k, z, arr))
