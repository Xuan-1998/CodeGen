def min_possible_length(n, arr):
    stack = []
    for num in arr:
        # Check if the current number can be merged with the top of the stack
        while stack and stack[-1] == num:
            stack.pop()
            num += 1
        stack.append(num)
    return len(stack)

# Read input from stdin
n = int(input())
arr = list(map(int, input().split()))

# Get the minimum possible length of the array
min_length = min_possible_length(n, arr)

# Print the result to stdout
print(min_length)
