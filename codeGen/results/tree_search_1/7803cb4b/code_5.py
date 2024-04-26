def min_array_length(arr):
    stack = []
    for num in arr:
        while stack and stack[-1] == num:
            stack.pop()
            num += 1
        if stack and stack[-1] + 1 == num:
            stack[-1] += 1
        else:
            stack.append(num)
    return len(stack)

# Read input from stdin
n = int(input())
arr = list(map(int, input().split()))

# Calculate and print the answer
print(min_array_length(arr))
