def min_possible_length(n, a):
    stack = []
    for elem in a:
        # Check if the stack is not empty and the top element is equal to the current element
        while stack and stack[-1] == elem:
            stack.pop()  # Remove the top element
            elem += 1    # Increment the current element
        stack.append(elem)  # Push the current element onto the stack
    return len(stack)  # The size of the stack is the answer

# Read input from stdin
n = int(input().strip())
a = list(map(int, input().strip().split()))

# Get the minimum possible length
result = min_possible_length(n, a)

# Print the result to stdout
print(result)
