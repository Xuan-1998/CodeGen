def max_problems(n, k, difficulties):
    left = 0
    right = n - 1
    count = 0
    
    while left <= right:
        if difficulties[left] <= k:
            left += 1
        elif difficulties[right] <= k:
            right -= 1
        else:
            break
            
    return min(left, right) + 1

n, k = map(int, input().split())
difficulties = list(map(int, input().split()))

print(max_problems(n, k, difficulties))
