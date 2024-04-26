from sys import stdin

def simulate_eating_process(n, a, k, b):
    stack = []
    actions = []
    j = 0  # Index for final queue
    
    for i in range(n):
        stack.append(a[i])
        while stack and j < k and stack[-1] == b[j]:
            # Match found, pop the stack and record the action
            stack.pop()
            actions.append(f"{len(stack) + 1} L")
            j += 1
        while len(stack) > 1 and j < k and stack[-1] + stack[-2] == b[j]:
            # Combine top two weights on the stack and record the action
            eaten = stack.pop()
            stack[-1] += eaten
            actions.append(f"{len(stack)} R")
            j += 1
        
        # Check if the current top of stack exceeds the required weight
        if stack and j < k and stack[-1] > b[j]:
            return "NO"
    
    # If we matched all weights in the final queue
    if j == k:
        return ["YES"] + actions
    else:
        return "NO"

# Read input from stdin
n = int(stdin.readline().strip())
a = list(map(int, stdin.readline().strip().split()))
k = int(stdin.readline().strip())
b = list(map(int, stdin.readline().strip().split()))

# Process and output the result
result = simulate_eating_process(n, a, k, b)
if result == "NO":
    print(result)
else:
    for line in result:
        print(line)
