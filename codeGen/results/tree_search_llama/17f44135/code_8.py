def solve():
    n, k = map(int, input().split())
    difficulties = list(map(int, input().split()))
    
    left, right = 0, n - 1
    solvable_count = 0
    
    while left <= right:
        if difficulties[left] <= k and difficulties[right] <= k:
            left += 1
            right -= 1
            solvable_count += 2
        elif difficulties[left] <= k:
            left += 1
        else:
            right -= 1
    
    print(solvable_count)

solve()
