def max_score():
    t = int(input())
    for _ in range(t):
        n, k, z = map(int, input().split())
        arr = list(map(int, input().split()))
        score = 0
        move_count = 0
        for i in range(1, n):
            if move_count < k:
                right_score = score + arr[i]
                left_score = score + arr[i-1]
                if move_count <= z or right_score > left_score:
                    score += arr[i]
                    move_count += 1
                else:
                    score += arr[i-1]
                    move_count -= 1
            else:
                break
        print(score)

max_score()
