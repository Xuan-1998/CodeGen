from collections import defaultdict

def max_points(a):
    n = len(a)
    
    # Handle edge cases
    if n == 0:
        return 0
    
    dp = defaultdict(int)  # memoization dictionary
    prev_elements = set()  # set to keep track of previous elements
    
    for i, x in enumerate(a):
        max_points = 0
        
        # calculate the maximum points if the current element is deleted
        for j in range(i-2, -1, -1):
            if a[j] != x and a[j] not in prev_elements:
                max_points = max(max_points, dp[(a[:j],)] + i - j)
                break
        
        # update memoization dictionary and previous elements set
        dp[(a[:i+1],)] = max_points
        prev_elements.add(x)
    
    return max_points

# Test your function
n = int(input())
a = [int(x) for x in input().split()]
print(max_points(a))
