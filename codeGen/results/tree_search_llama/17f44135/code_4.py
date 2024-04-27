def max_problems_solved():
    n, k = map(int, input().split())
    difficulties = list(map(int, input().split()))
    
    left, right = 0, n - 1
    solved_problems = 0
    
    while True:
        if left <= right and difficulties[left] <= k:
            left += 1
        elif left <= right and difficulties[right] <= k:
            right -= 1
        else:
            break
        
    return n - (right - left + 1)

print(max_problems_solved())
