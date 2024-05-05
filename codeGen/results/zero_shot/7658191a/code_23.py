def max_score(arr, k, z):
    n = len(arr)
    score = 0
    moves_to_left = 0

    for i in range(k):
        if i % (z + 1) == 0:  # move to left
            score += arr[i - 1]
            moves_to_left += 1
        else:  # move to right
            score += arr[i]

    return score

t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    arr = list(map(int, input().split()))
    print(max_score(arr, k, z))
