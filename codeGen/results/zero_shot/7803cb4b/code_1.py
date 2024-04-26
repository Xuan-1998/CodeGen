def min_possible_length(n, arr):
    stack = []
    for num in arr:
        # Check if the current element can be merged with the element on top of the stack
        while stack and stack[-1] == num:
            stack.pop()
            num += 1
        stack.append(num)
    return len(stack)

# Read input from stdin
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# Get the minimum possible length and print it
min_length = min_possible_length(n, arr)
print(min_length)
