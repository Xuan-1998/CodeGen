def solve_problems():
    n, k = map(int, input().split())
    difficulties = sorted([int(x) for x in input().split()], reverse=True)
    
    left, right = 0, n-1
    count = 0
    
    while left <= right:
        if difficulties[left] <= k or difficulties[right] <= k:
            if difficulties[left] <= k:
                left += 1
            else:
                right -= 1
            count += 1
        elif difficulties[left] > difficulties[right]:
            left += 1
        else:
            right -= 1
    
    return count

print(solve_problems())
