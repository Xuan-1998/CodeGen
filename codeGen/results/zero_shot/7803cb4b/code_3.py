def min_possible_length(n, arr):
    stack = []
    
    for num in arr:
        # Check if the current number can be combined with the top of the stack
        while stack and stack[-1] == num:
            stack.pop()  # Remove the top element
            num += 1     # Increment the current number
        stack.append(num)  # Push the current (possibly incremented) number
    
    return len(stack)

# Read input from stdin
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# Get the result and print it to stdout
result = min_possible_length(n, arr)
print(result)
