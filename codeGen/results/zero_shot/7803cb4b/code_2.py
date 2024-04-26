def min_possible_length(n, a):
    stack = []
    for num in a:
        while stack and stack[-1] == num:
            stack.pop()
            num += 1
        stack.append(num)
    return len(stack)

# Read input from stdin
n = int(input().strip())
a = list(map(int, input().strip().split()))

# Get the minimum possible length
result = min_possible_length(n, a)

# Print the result to stdout
print(result)
