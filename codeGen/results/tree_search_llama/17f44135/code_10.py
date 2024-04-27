def max_solvable_problems():
    n, k = map(int, input().split())
    difficulties = list(map(int, input().split()))
    left, right = 0, n-1
    solvable_problems = 0

    while left <= right:
        if difficulties[left] <= k and difficulties[right] <= k:
            solvable_problems += 2
            left += 1
            right -= 1
        elif difficulties[left] <= k:
            solvable_problems += 1
            left += 1
        else:
            solvable_problems += 1
            right -= 1

    print(solvable_problems)

max_solvable_problems()
