from collections import deque

def canJump(nums):
    n = len(nums)
    max_reachable_index = 0
    memo = { (0, -1): True }  # Initialize memoization table with default values
    
    queue = deque([(0, 0)])  # Initialize queue-based approach
    
    while queue:
        current_index, max_reachable_index = queue.popleft()
        
        if current_index == n - 1:  # If we have reached the last index
            return True
        
        for i in range(current_index + 1, min(current_index + nums[current_index] + 1, n)):
            new_max_reachable_index = max(max_reachable_index, i)
            
            if (i, new_max_reachable_index) not in memo:  # If this subproblem is not visited yet
                queue.append((i, new_max_reachable_index))  # Add it to the queue
            
            if (i, new_max_reachable_index) in memo and memo[(i, new_max_reachable_index)]:
                return False
        
    return False

# Test your solution here
nums = list(map(int, input().split()))
print(canJump(nums))
