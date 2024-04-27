def solve_problems():
    n, k = map(int, input().split())
    problems = list(map(int, input().split()))
    problems.sort()
    
    left = 0
    right = n - 1
    solved = 0
    
    while True:
        if problems[left] <= k:
            k -= problems[left]
            left += 1
            solved += 1
        elif problems[right] <= k:
            k -= problems[right]
            right -= 1
            solved += 1
        else:
            break
            
    return n - solved

print(solve_problems())
