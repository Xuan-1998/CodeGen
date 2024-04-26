n, k = map(int, input().split())
problems = list(map(int, input().split()))

left_pointer, right_pointer = 0, n-1

solutions = 0

while left_pointer <= right_pointer:
    if problems[left_pointer] <= k and problems[right_pointer] <= k:
        solutions += 1
        left_pointer += 1
        right_pointer -= 1
    elif problems[left_pointer] <= k:
        solutions += 1
        left_pointer += 1
    else:
        solutions += 1
        right_pointer -= 1

print(solutions)
