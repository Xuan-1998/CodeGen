def min_array_length(n, a):
    stack = []
    for elem in a:
        if stack and stack[-1][0] == elem:
            # Increment the value and merge
            value, count = stack.pop()
            elem += 1
            # Pop the stack until the top element is not equal to the incremented value
            while stack and stack[-1][0] == elem:
                stack.pop()
        stack.append((elem, 1))
    return len(stack)

# Read input from stdin
n = int(input().strip())
a = list(map(int, input().strip().split()))

# Output the answer to stdout
print(min_array_length(n, a))
