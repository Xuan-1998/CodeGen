def max_problems_to_solve():
    n, k = map(int, input().split())
    difficulties = list(map(int, input().split()))
    
    left, right = 0, n - 1
    solved = 0
    
    while left <= right:
        if difficulties[left] <= k and (right == n - 1 or difficulties[right] > k):
            solved += 1
            if left < right:
                left += 1
            else:
                break
        elif difficulties[right] <= k and (left == 0 or difficulties[left] > k):
            solved += 1
            if left < right:
                right -= 1
            else:
                break
        else:
            left += 1
            right -= 1
    
    print(solved)

max_problems_to_solve()
