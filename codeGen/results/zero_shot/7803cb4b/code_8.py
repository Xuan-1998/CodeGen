def find_min_length(arr):
    stack = []
    for num in arr:
        if stack and stack[-1][0] == num:
            stack[-1][1] += 1
            while stack and stack[-1][1] == stack[-1][0]:
                val, _ = stack.pop()
                if stack and stack[-1][0] == val + 1:
                    stack[-1][1] += 1
                else:
                    stack.append([val + 1, 1])
        else:
            stack.append([num, 1])
    return sum(count for _, count in stack)

# Read input
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# Find the minimum length
min_length = find_min_length(arr)

# Print the result
print(min_length)
