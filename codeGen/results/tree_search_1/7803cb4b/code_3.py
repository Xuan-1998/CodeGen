n = int(input())
a = list(map(int, input().split()))

def min_length_after_operations(a):
    stack = []
    for num in a:
        while stack and stack[-1] == num:
            stack.pop()
            num += 1
        stack.append(num)
    return len(stack)

print(min_length_after_operations(a))
