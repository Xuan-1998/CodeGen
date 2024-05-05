def max_score():
    t = int(input())
    for _ in range(t):
        n, k, z = map(int, input().split())
        arr = list(map(int, input().split()))
        rightward_moves = min(k, z)
        leftward_moves = min(k - rightward_moves, z)
        score_right = sum(arr[1:n-rightward_moves+1])
        score_left = sum(arr[1:n-leftward_moves+1])
        print(max(score_right, score_left))

max_score()
